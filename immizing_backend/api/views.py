from django.shortcuts import render, HttpResponse
import requests
import environ
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import FNSerializer,AddressSerializer
from .models import *

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
    presentAddrData=data['present']
    copyPresToPrev=data['copyPresToPrev']
    if ('mailingaddr' in data):
        mailingAddrData=data['mailingaddr']
        addrserializer=AddressSerializer(data=mailingAddrData)
        if addrserializer.is_valid():
            addrserializer.save()
    addrserializer=AddressSerializer(data=presentAddrData)
        
    if addrserializer.is_valid():
        addrserializer.save()


    presentAddr=Address.objects.filter(Street=presentAddrData['Street'],city=presentAddrData['city'],state=presentAddrData['state'],zip_code=presentAddrData['zip_code']).first()
    
    ForeignNationalInfo.objects.create(
        FirstName=data['FirstName'],LastName=data['LastName'],Date_of_Birth=data['Date_of_Birth'],Email=data['Email'],Phone=data['Phone'],SSN=data['SSN'],presentAddress=presentAddr)
    myinfoObj=ForeignNationalInfo.objects.get(SSN=data['SSN'])
    if copyPresToPrev==True:
        myinfoObj.previousAddresses.add(presentAddr)
        print("same as present")
    else:
        previousAddrData=data['previous']
        addrserializer=AddressSerializer(data=previousAddrData)
        if addrserializer.is_valid():
            addrserializer.save()

        previoustAddr=Address.objects.filter(Street=previousAddrData['Street'],city=previousAddrData['city'],state=previousAddrData['state'],zip_code=previousAddrData['zip_code']).first()
        myinfoObj.previousAddresses.add(previoustAddr)
        print("previous add")
    context={
        "success":True,
        "success_code":200,
        "message":"My info was saved",
        

    }
    return Response(context)
    # else:
    #     return Response("not created")
    

