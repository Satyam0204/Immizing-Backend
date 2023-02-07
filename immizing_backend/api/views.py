from django.shortcuts import render, HttpResponse

def home(request):
    print("home")
    return HttpResponse('hello')
