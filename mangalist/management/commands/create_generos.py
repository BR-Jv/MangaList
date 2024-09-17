from django.core.management import BaseCommand
from mangalist.models import Genero

generos = [
    "Ação",
    "Aventura",
    "Fantasia",
    "Drama",
    "Romance",
    "Suspense",
    "Artes Marciais",
    "Comédia",
    "Demônios",
    "Ecchi",
    "Escolar",
    "Esporte",
    "Ficção científica",
    "Harém",
    "Histórico",
    "Horror",
    "Jogo",
    "Light Novel",
    "Magia",
    "Mecha",
    "Militar",
    "Mistério",
    "Musical",
    "Samurai",
    "Slice of Life",
    "Sobrenatural",
    "Super Poderes",
    "Terror"
]

class Command(BaseCommand): 
    help = ''


    def handle(self, *args, **kwargs):
        for genero in generos:
            Genero.objects.get_or_create(nome=genero)
        


         
     
