from django.urls import path

from .apis import UserList, UserDetail


urlpatterns = [
    path('', UserList.as_view()),
    path('', UserDetail.as_view()),
]

