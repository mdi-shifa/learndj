from django.urls import path

from . import views


urlpatterns = [ 
    #'' is a call for homepage
    path('register/',views.register, name='register'),
    path('login/',views.login,name='login')
]
