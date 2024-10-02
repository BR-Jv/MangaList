from django.contrib import admin

from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user__first_name', 'user__username',]
    pass

