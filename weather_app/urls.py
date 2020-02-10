from django.urls import path 
from . import views
from django.conf.urls import handler500
  
urlpatterns = [ 
         
          path('base/', views.base ),
          path('', views.index),
] 

