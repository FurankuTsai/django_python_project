from .repositories import UserRepository
from .embedding_service import EmbeddingService
from .vector_repository import VectorRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        self.embedding = EmbeddingService()
        self.vector_repo = VectorRepository()
        
    def list_users(self):
        return self.repo.get_all()

    def get_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def create_user(self, data: dict):

       # 1. 存 MySQL
       user = self.repo.create(data)

       # 2. 組合要給 AI 的文字
       text = f"""
       Name: {user.name}
       Bio: {user.bio}
       """

       # 3. 產生向量
       vector = self.embedding.create(text)

       # 4. 存 Qdrant
       self.vector_repo.save(
           user.id,
           vector,
           text
       )

       return user
    
    def update_user(self, user_id: int, data: dict):
        user = self.get_user(user_id)
        return self.repo.update(user, data)

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        self.repo.delete(user)

    def search_users(self, keyword):
        # 1. 搜尋文字轉向量
        vector = self.embedding.create(keyword)

        # 2. 去 Qdrant 找相似資料
        result = self.vector_repo.search(vector)

        return result
