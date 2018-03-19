from django.urls import include, path

app_name = 'snippets'
urlpatterns = [
    path('api-view/', include('snippets.urls.api_view')),
    path('mixins/', include('snippets.urls.mixins')),
    path('generic/', include('snippets.urls.generic')),
]
