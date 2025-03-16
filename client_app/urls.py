from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_doctors, name='search_doctors'),
    
     
]
