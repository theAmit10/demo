from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator # used in paginator process.
# this is used to check .
from listings.choices import price_choices, bedroom_choices, state_choices
from .models import Listing

# Create your views here. 
# here we are fetching data from database. this is the first part of pagination after this we have to go in listings.html.
# check out the 1st screenshot SS without pagination -> pagination is used to prev page or next page etc. 
def listings(request):
    #listings = Listing.objects.all() # its shows a problem that class Listing has no object member . its going to fixed with -> pip install pylint-django  after that we have create a .pylintrc file -> pylint --generate-rcfile > .pylintrc -> in which we add this code -> "python.linting.pylintArgs": ["--load-plugins", "pylint_django"]
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # due to this now in the listings tab , items will show acording to uplaoded date and from admin area if we make published false than it will be disappear.
    # this all are required for the pagination ...look in documentation.
    paginator = Paginator(listings, 3) # here 1st args is the thing which are commingfrom the database and 2nd args is to show how many number of element of that we want to show in a single page.
    page = request.GET.get('page') # 'page' is the url parameter of that page.
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    } 
    return render(request, 'listings/listings.html', context= context)

# after doing this only we can create a dynamic page where data are fetched by database. from listing.html
def listing(request, listing_id):
    # for a particular listing page for this we have to import get_object_or_404
    listing = get_object_or_404(Listing, pk=listing_id) # here pk is a primary key used for listing id.
    # because of get_object_or_404 if we add invalid listing_id than we get page not found page.
    context = {
        'listing' : listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # getting keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) # description__icontains= this will check the simialr type of word in the databse which is similar to keywords. in which __icontains is used to find the similar type of words.

    # searchiing through city name 
    if 'city' in request.GET:
        city = request.GET['city'] # in server this is checking name which have 'city' as its name. its checking name attribute in the server site.
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) # here iexact means i = because of i it becomse not case sensitive 
    
    # searchiing through state name 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # searchiing through bedrooms name 
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)# lte = less than or equal to

    # searchiing through price name 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices, # this used 
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values' : request.GET # this is used to hold the values in the search field .
    } 

    return render(request, 'listings/search.html', context)
