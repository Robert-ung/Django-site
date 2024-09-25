import datetime
from django.db import models

class Pokemon(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    generation = models.IntegerField(default=1)
    couleur = models.CharField(max_length=50)
    poids = models.FloatField()
    hauteur = models.FloatField()
    photo = models.ImageField(upload_to="photos")
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom
