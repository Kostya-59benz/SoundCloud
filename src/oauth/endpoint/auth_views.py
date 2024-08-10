from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
from ..services.google import check_google_auth
from .. import serializer

def google_login(request):

    return render(request,  'oauth/google_login.html')



@api_view(['POST'])
def google_auth(request):
    """ Accepting authorization from Google"""
    google_data = serializer.GoogleAuth(data=request.data)
    if google_data.is_valid():
        token = check_google_auth(google_data.data)
        return Response(token)
    else:
        AuthenticationFailed(code=403, detail='Bad data google')
