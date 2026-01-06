from django.http import HttpResponse # type: ignore

def hello(request):
    return HttpResponse("Hello from users app 👋")