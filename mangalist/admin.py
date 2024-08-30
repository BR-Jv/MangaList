from django.contrib import admin

from .models import * 


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin): 
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name']