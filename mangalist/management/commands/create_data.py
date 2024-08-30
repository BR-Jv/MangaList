from django.core.management import BaseCommand
from mangalist.models import Autor

class Command(BaseCommand): 
    help = 'Carregando informações'

    def handle(self, *args, **kwargs):
        # Autores
        Autor.objects.get_or_create(first_name = 'Eiichiro', last_name='Oda')
        Autor.objects.get_or_create(first_name = 'Masashi', last_name='Kishimoto')
        Autor.objects.get_or_create(first_name = 'Gege', last_name='Akutami')
        Autor.objects.get_or_create(first_name = 'Akira', last_name='Toriyama')
        Autor.objects.get_or_create(first_name = 'Tite', last_name='Kubo')
        Autor.objects.get_or_create(first_name = 'Yoshihiro', last_name='Togashi')
        
        


         
     
