from apps.users.services import UserService
from .llm_service import LLMService


class ChatService:

    def __init__(self):
        self.user_service = UserService()
        self.llm = LLMService()


    def chat(self, message):

        users = self.user_service.search_users(message)

        context = self.build_context(users)

        answer = self.llm.generate(
            message,
            context
        )

        return {
            "message": message,
            "answer": answer,
            "results": users
        }


    def build_context(self, users):

        context = ""

        for user in users:
            context += f"""
                工程師姓名: {user['name']}
                技能背景: {user['bio']}
                匹配度: {user['score']}
                """

        return context