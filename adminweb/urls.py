from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('WellCome/' , views.WellCome , name='WellCome'),
   path('', views.login , name='login'),
   path('logout/', views.logout, name='logout'),
   path('content/', views.content, name='content'),
   path('dashboard/' , views.dashboard, name='dashboard'),    
]

