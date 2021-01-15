from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing # used to catch the files from the listing models .
from relators.models import Relator # used for about page 
from listings.choices import price_choices, bedroom_choices, state_choices # here this is used in to catch the choices . this is use din searching processss.

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # [:3] means in index page only threee listner will be shown .

    context = {
        'listings': listings,
        'state_choices': state_choices, # this used 
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    } 

    return render(request, 'pages/index.html', context)


def about(request):
    # getting all the relators
    relators = Relator.objects.order_by('-hire_date')

    # geetting mvp relator
    mvp_relator = Relator.objects.all().filter(is_mvp=True)

    context = {
        'relators': relators,
        'mvp_relators': mvp_relator
    }

    return render(request, 'pages/about.html', context)