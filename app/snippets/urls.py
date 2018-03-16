from django.urls import path

from . import views

app_name = 'snippets'
urlpatterns = [
    path('', views.SnippetList.as_view()),
]
