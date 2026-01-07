from .repositories import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def list_users(self):
        return self.repo.get_all()

    def get_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def create_user(self, data: dict):
        return self.repo.create(data)

    def update_user(self, user_id: int, data: dict):
        user = self.get_user(user_id)
        return self.repo.update(user, data)

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        self.repo.delete(user)
