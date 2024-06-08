from django.urls import path
from . import views 
urlpatterns = [ 
    path('list/', views.show_lists, name='show_lists'),
     ]             
