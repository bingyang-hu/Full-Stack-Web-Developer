from django.contrib import admin

# Register your models here.


from . import models


class MovieAdmin(admin.ModelAdmin): #m aodelname+'admin'

    fields = ['release_year','title','length']  # title,length,release year is the original order

    search_fields= ['title']

    list_filter= ['release_year','length']

    list_display = ['title','release_year','length']

admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)
