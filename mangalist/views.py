from django.views.generic import ListView, DetailView
from .models import Manga

class MangasListView(ListView):
    model = Manga

class MangasDetailView(DetailView):
    model = Manga

