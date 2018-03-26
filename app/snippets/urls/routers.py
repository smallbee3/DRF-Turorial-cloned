from django.urls import include, path
from rest_framework.routers import DefaultRouter

from snippets.apis.viewsets import SnippetViewSet


# 라우터를 생성하고 뷰셋을 등록합니다

router = DefaultRouter()
router.register(r'', SnippetViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
# 안감싸도 됨.


# 3/19
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# 이 부분이 urls/viewsets.py처럼 써줄 수 없기 때문에
# 이것을 apis/viewsets.py 에서 @detail_route를 사용해서
# 직접 정의함
