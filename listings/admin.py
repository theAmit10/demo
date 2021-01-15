from django.contrib import admin

# Register your models here.

from .models import Listing

# here ListingAdmin(admin.ModelAdmin) is used to modify the listing admin page
# if you dont want to modify any kind of such pages than you can just write this code in these page.

# from django.contrib import admin
# from .models import Listing
# admin.site.register(Listing) 

# this class is used to edit the listing page

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'price', 'list_date', 'relator')
    list_display_links = ('id', 'title')
    list_filter = ('relator',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin) 