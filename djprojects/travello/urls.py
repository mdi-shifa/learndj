from django.urls import path

from . import views


urlpatterns = [ 
    #'' is a call for homepage
    path('',views.index, name="index"),
]
