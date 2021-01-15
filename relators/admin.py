from django.contrib import admin

# Register your models here.
# here we are setting relator as a part of our admin area.
from .models import Relator

# here RelatorAdmin(admin.ModelAdmin) is used to modify the relator admin page
# if you dont want to modify any kind of such pages than you can just write this code in these page.

# from django.contrib import admin
# from .models import Relator
# admin.site.register(Relator) 

# this class is used to edit the relator page

class RelatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Relator, RelatorAdmin)