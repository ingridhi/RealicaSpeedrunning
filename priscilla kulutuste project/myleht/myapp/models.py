from django.db import models

# Create your models here.

class Transaction(models.Model):

    
    saatja = models.CharField(max_length=150)
    saaja = models.CharField(max_length=150)
    summa = models.FloatField()
    dt = models.DateTimeField('date sent')

    def __str__(self):
        return f'{self.saatja} > {self.saaja}: {self.summa}' 

    