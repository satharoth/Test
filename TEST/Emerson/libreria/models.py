from django.db import models

# Create your models here.

class Libreria(models.Model):
    ID = models.AutoField(primary_key=True)
    Libro = models.CharField(max_length=150)
    Autor = models.CharField(max_length=150)
    Editorial = models.CharField(max_length=150)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.Libro,self.Autor)
