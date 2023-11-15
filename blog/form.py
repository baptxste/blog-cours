from django import forms
from .models import Joueur  





class createplayer(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['numero','nom','poste','photo','lieu']