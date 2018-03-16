from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer

__all__ = (
    'SnippetList',
)


class SnippetList(APIView):
    # /snippets/ <- 에 매칭되도록 urls모듈 작성
    #                   app_name이 'snippets'여야 함
    #
    # config.urls
    #   include('snippets.urls')
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
