from django.shortcuts import render, HttpResponse
import requests
import environ
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import FNSerializer,AddressSerializer


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()



def get_access_token():
    url="https://api-int.uscis.gov/oauth/accesstoken"

    headers={
        'content-type': 'application/x-www-form-urlencoded'
    }
    payload={
        'grant_type':'client_credentials',
        'client_id':env('CLIENT_ID'),
        'client_secret':env('CLIENT_SECRET')
    }
    response = requests.post(url,headers=headers,data=payload)
    data = response.json()
    access_token=data['access_token']
    print(access_token)

def home(request):
    print("home")
    get_access_token()
    return HttpResponse('hello')


@api_view(['POSt'])
def createMyInfo(request):
    data=request.data
    presentAddr=data['present']
    addrserializer=AddressSerializer(data=presentAddr)
        
    if addrserializer.is_valid():
        addrserializer.save()
        return Response("present address was saved")
    else:
        return Response("not created")
    

