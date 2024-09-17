from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Manga

class MangasListView(ListView):
    model = Manga

class MangasDetailView(DetailView):
    model = Manga

class MangasUpdateView(UpdateView):
    model = Manga
    fields = '__all__'
    template_name_suffix = "_update"

class MangasDeleteView(DeleteView):
    model = Manga
    success_url = reverse_lazy("mangas-list")
    template_name_suffix = "_delete"

class MangasCreateView(CreateView):
    model = Manga
    fields = '__all__'
    template_name_suffix = "_create"
