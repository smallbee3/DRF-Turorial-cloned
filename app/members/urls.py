from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .apis import UserList, UserDetail

app_name = 'members'
urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
