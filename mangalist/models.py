from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    
    def fullName(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta: 
        abstract = True

class Autor(Person): 
    
    def __str__(self) -> str:
        return self.fullName()

class Ilustrador(Person):
    first_name = models.CharField(max_length=75, null=True, blank=True)
    last_name = models.CharField(max_length=75, null=True, blank=True)
     
    def __str__(self) -> str:
        return self.fullName()

class Manga(models.Model):
    pass 

class Categoria(models.Model):
    pass 

class Status(models.Model):
    pass 

class Genero(models.Model):
    pass 
