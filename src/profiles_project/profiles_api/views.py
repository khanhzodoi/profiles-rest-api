from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.
class HelloAPIView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIview features."""
        an_apivew = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a tradiontional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        
        return Response({'message': 'hello', 'an_apiview': an_apivew})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)


        if serializer.is_valid():
            name = serializer.data.get('name')
            email = serializer.data.get('email')
            message = 'Hello {0} and your email is {1}'.format(name,email)
            return Response({'message': message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Handles updating an object."""
        
        return Response({'method': 'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete an object."""

        return Response({'method': 'delete'})