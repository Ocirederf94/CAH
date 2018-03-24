from django.shortcuts import render
from django.template.context_processors import request
from django.http.response import HttpResponse


def loginTest(request):
    return  HttpResponse("<h2> Login </h2>")


def login(request):
    return render(request, 'loginModule/login.html')

def register(request):
    return render(request, 'loginModule/register.html')



    
    
