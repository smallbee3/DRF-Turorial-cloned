
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRoot(APIView):
    def get(self, request, format=None):

        data = {
            'users': reverse('members:user-list', request=request, format=format),
            'snippets': reverse('snippets:snippet-list', request=request, format=format),
        }
        return Response(data)