from django.db import models
from django.urls import reverse

class Ilustrador(models.Model):
    first_name = models.CharField(max_length=95, null=False, blank=False)
    last_name = models.CharField(max_length=95, null=False, blank=True, default=" ")
    
    class Meta: 
        verbose_name = 'Ilustrador'
        verbose_name_plural = "Ilustradores"
    
    def fullName(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.fullName()

class Autor(models.Model):
    first_name = models.CharField(max_length=95, null=False, blank=False)
    last_name = models.CharField(max_length=95, null=False, blank=True, default=" ")
    
    class Meta: 
        verbose_name = 'Autor'
        verbose_name_plural = "Autores"
    
    def fullName(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.fullName()

STATUS = (
    ('l', 'Em lançamento'),
    ('h', 'Em hiato'),
    ('f', 'Finalizado'),
)

class Manga(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    volumes = models.IntegerField(null=True, blank=True)
    capitulos = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='f') 
    data_lancamento = models.DateField(verbose_name="Data de lançamento") 
    data_encerramento = models.DateField(null=True, blank=True, verbose_name="Data de encerramento")
    autor = models.ForeignKey('Autor', on_delete=models.DO_NOTHING, related_name='mangas')
    ilustrador = models.ForeignKey('Ilustrador', on_delete=models.DO_NOTHING, related_name='ilustrador', null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING, related_name='catManga', null=True, blank=True)
    generos = models.ManyToManyField('Genero', related_name='genManga')

    class Meta: 
        verbose_name = 'Mangá'
        verbose_name_plural = "Mangás"

    def __str__(self) -> str:
        return self.nome 

    def get_absolute_url(self):
        return reverse("mangas-detail", kwargs={"pk": self.pk})
    
    

class Categoria(models.Model):
    nome = models.CharField(max_length=55, unique=True, null=False, blank=False)

    class Meta: 
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=55, unique=True, null=False, blank=False)

    class Meta: 
        verbose_name = 'Genero'
        verbose_name_plural = "Generos"

    def __str__(self) -> str:
        return self.nome