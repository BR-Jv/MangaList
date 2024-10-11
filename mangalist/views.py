from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Manga
from account.models import Perfil

class MangasListView(ListView):
    model = Manga


class MangasDetailView(DetailView):
    model = Manga

    

class MangasUpdateView(LoginRequiredMixin, UpdateView):
    model = Manga
    fields = '__all__'
    template_name_suffix = "_update"

class MangasDeleteView(LoginRequiredMixin, DeleteView):
    model = Manga
    success_url = reverse_lazy("mangas-list")
    template_name_suffix = "_delete"

class MangasCreateView(LoginRequiredMixin, CreateView):
    model = Manga
    fields = '__all__'
    template_name_suffix = "_create"


class FavoritoListView(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = "mangalist/favoritos_list.html"

    