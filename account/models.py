from django.db import models
from django.contrib.auth.models import User

from mangalist.models import Manga

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favoritos = models.ManyToManyField(Manga, verbose_name="Favoritos", related_name="Users")

    def __str__(self) -> str:
        return self.user.first_name
    

    