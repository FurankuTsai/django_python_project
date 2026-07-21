from apps.users.services import UserService


class ChatService:

    def __init__(self):
        self.user_service = UserService()


    def chat(self, message):

        users = self.user_service.search_users(message)

        return {
            "message": message,
            "results": users
        }