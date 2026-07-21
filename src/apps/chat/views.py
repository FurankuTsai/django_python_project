import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .services import ChatService


@method_decorator(csrf_exempt, name='dispatch')
class ChatView(View):

    service = ChatService()

    def post(self, request):

        data = json.loads(request.body)

        message = data.get("message")

        if not message:
            return JsonResponse(
                {
                    "error": "message is required"
                },
                status=400
            )

        result = self.service.chat(message)

        return JsonResponse(result)