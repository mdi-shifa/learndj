from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #function to call homepage and return hello world
    #we can call any name dynamically
    return render(request,'home.html',{'name':'shifa'})