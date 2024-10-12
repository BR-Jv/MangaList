from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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

class FavoritoRedirectView(RedirectView):
    url = reverse_lazy('mangas-list')

    def get_redirect_url(self, *args, **kwargs):
        #print(self.request.user)
        
        perfil = get_object_or_404(Perfil, user=self.request.user)

        manga = get_object_or_404(Manga, pk=kwargs['pk'])

        
        for i in perfil.favoritos.all():
           
            if i == manga : 
                perfil.favoritos.remove(manga)
                return super().get_redirect_url(*args, **kwargs)

        perfil.favoritos.add(manga)
        return super().get_redirect_url(*args, **kwargs)

        
    