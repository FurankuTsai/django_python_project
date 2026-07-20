from django.urls import path
from .views import UserView, UserSearchView

urlpatterns = [
    path("search/", UserSearchView.as_view()),
    path("", UserView.as_view()),
    path("<int:user_id>/", UserView.as_view()),
]