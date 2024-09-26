from django.contrib import admin

from .models import * 

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'autor', 'status',]
    list_display_links = ['nome']
    list_filter = ['status', 'generos']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ['nome']


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ['nome']

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['first_name', ]
    list_display_links = ['first_name', ]

@admin.register(Ilustrador)
class IlustradorAdmin(admin.ModelAdmin):
    list_display = ['first_name', ]
    list_display_links = ['first_name', ]
