from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('WellCome/' , views.WellCome , name='WellCome'),
   path('', views.login , name='login'),
   path('logout/', views.logout, name='logout'),
   path('content/', views.content, name='content'),
   path('content1/', views.content1, name='content1'),
   path('dashboard/' , views.dashboard, name='dashboard'),    
   ####################################################################
   path('add_content/' , views.add_content, name='add_content'),
   path('content_list/' , views.content_list, name='content_list'), 
   path('edit_content/<str:id>/' , views.edit_content, name='edit_content'),
   path('delete_content/<str:id>/' , views.delete_content, name='delete_content'), 
]

