from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers


class HelloApiView(APIView):

    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})


    def post(self, request):
        """Create a Hello Message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} '
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
             )

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP method as function(get,post,put,patch)',
        'is similar to a traditional Django View',
        'gives you the mostr control of application logic',
        'is mapped manually to URLS'
        ]
        return Response({'Message':'Hello','an_apiview':an_apiview})
