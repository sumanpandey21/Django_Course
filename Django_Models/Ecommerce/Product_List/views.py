from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("I am product home.")

def type(request):
    return HttpResponse("I am product type.")