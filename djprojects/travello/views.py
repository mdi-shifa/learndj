from django.shortcuts import render
from .models import destination
# Create your views here.
def index(request):
    dest1= destination()
    dest1.name= 'bangalore'
    dest1.description= 'the IT city'
    dest1.img= 'destination_1.jpg'
    dest1.price= 900

    dest2= destination()
    dest2.name= 'Kerela'
    dest2.description= 'a city of nature'
    dest2.img= 'destination_2.jpg'
    dest2.price= 1000

    dest3= destination()
    dest3.name= 'hyderabad'
    dest3.description= 'a city of nawabs'
    dest3.img= 'destination_3.jpg'
    dest3.price= 800

    dests=[dest1,dest2,dest3]
    return render(request,"index.html", {'dests': dests} )
     
     
     
