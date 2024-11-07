from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #to print hello world in homepage
    return HttpResponse("hello world")