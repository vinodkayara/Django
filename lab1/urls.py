

from django.urls import path

from lab1 import views

urlpatterns =[path('datetime/',views.current_datetime,name='current_datetime')]