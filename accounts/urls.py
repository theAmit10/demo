from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'), # settinf path to render page  here '' means /listing page
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
    
]     