from django.shortcuts import render

from rest_framework .views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    
    def get(self,request,format=None):
        """returns a list of APIView features"""
        an_apiview = [
        'uses HTTP methods functions(get,post,put,patch,delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLS',

        ]

        return Response({'message':"Hello","an_apiview":an_apiview})
