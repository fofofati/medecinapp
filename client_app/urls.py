from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_doctors, name='search_doctors'),
    path('public_doctors/', views.public_doctors, name='public_doctors'),
    path('about/', views.about, name='about'),
    path('search/doctors/', views.search_doctors, name='search_doctors'),

  
     
]
