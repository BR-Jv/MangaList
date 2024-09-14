from django.db import models


class Ilustrador(models.Model):
    first_name = models.CharField(max_length=95, null=False, blank=False)
    last_name = models.CharField(max_length=95, null=True, blank=True)
    
    class Meta: 
        verbose_name = 'Ilustrador'
        verbose_name_plural = "Ilustradores"
    
    def fullName(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.fullName()

class Autor(models.Model):
    first_name = models.CharField(max_length=95, null=False, blank=False)
    last_name = models.CharField(max_length=95, null=True, blank=True)
    
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
    nome = models.CharField(max_length=255, unique=True, null=False, blank=False)
    volumes = models.IntegerField(null=True, blank=True)
    capitulos = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='f') 
    data_lancamento = models.DateField(null=False, blank=False) 
    data_encerramento = models.DateField()
    autor = models.ForeignKey('Autor', on_delete=models.DO_NOTHING, related_name='mangas')


    class Meta: 
        verbose_name = 'Mangá'
        verbose_name_plural = "Mangás"

    def __str__(self) -> str:
        return self.nome 


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