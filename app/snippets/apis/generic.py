from rest_framework import mixins, generics, permissions, renderers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from snippets.permissions import IsOwnerOrReadOnly
from ..serializers import SnippetSerializer
from ..models import Snippet


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    pagination_class = StandardResultsSetPagination

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


# 코드 조각의 하이라이트 버전에 대한 엔드 포인트 만들기
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (
        renderers.StaticHTMLRenderer,
    )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)