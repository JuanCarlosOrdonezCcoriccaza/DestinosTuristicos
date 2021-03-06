from django.db import models

# Create your models here.

class Destino(models.Model):

    name  = models.CharField(max_length=100)
    img   = models.ImageField(upload_to='pics',null=False)
    desc  = models.TextField()
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    state = models.BooleanField(default=True)

