from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # settinf path to render page
    path('about', views.about, name='about'),
    
] 