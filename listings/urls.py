from django.urls import path

from . import views

urlpatterns = [
    path('', views.listings, name='listings'), # settinf path to render page  here '' means /listing page
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    
] 