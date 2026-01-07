from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from .services import UserService

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    service = UserService()

    def get(self, request, user_id=None):
        if user_id:
            try:
                user = self.service.get_user(user_id)
                return JsonResponse({
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "bio": user.bio,
                })
            except ValueError as e:
                return JsonResponse({"error": str(e)}, status=404)

        users = self.service.list_users()
        return JsonResponse(list(users.values()), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        user = self.service.create_user(data)
        return JsonResponse({"id": user.id}, status=201)

    def put(self, request, user_id=None):
        data = json.loads(request.body)

        if user_id is None:
            return JsonResponse({"error": "user_id required in URL"}, status=400)

        try:
            user = self.service.update_user(user_id, data)
            return JsonResponse({"id": user.id})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)

    def delete(self, request, user_id):
        try:
            self.service.delete_user(user_id)
            return JsonResponse({}, status=204)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
