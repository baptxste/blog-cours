from django.conf import settings
from django.db import models
from django.utils import timezone
 
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    placemax = models.IntegerField()
    def __str__(self):
        return self.id_equip
 
 
class Joueur(models.Model):
    numero= models.CharField(max_length=100, primary_key=True) #numero de maillot unique
    nom = models.CharField(max_length=50)
    poste = models.CharField(max_length=20) 
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.numero