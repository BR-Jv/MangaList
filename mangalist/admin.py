from django.contrib import admin

from .models import * 

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['nome',]
    list_display_links = ['nome']


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
    pass
