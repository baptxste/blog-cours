from django import forms
from .models import Joueur  

class testf(forms.ModelForm):
    class Meta : 
        model = Joueur
        fields = ['numero', 'nom', 'poste', 'photo', 'lieu']



class modifnom(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom']