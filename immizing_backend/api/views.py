from django.shortcuts import render, HttpResponse
import requests
import environ
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
