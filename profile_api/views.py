from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP method as function(get,post,put,patch)',
        'is similar to a traditional Django View',
        'gives you the mostr control of application logic',
        'is mapped manually to URLS'
        ]
        return Response({'Message':'Hello','an_apiview':an_apiview})
