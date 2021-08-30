from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIview features."""
        an_apivew = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a tradiontional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        
        return Response({'message': 'hello', 'an_apiview': an_apivew})