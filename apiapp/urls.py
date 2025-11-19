from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('WellComeapi/' , views.WellCome , name='WellCome'),
]

