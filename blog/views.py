from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipement, Joueur
from django.utils import timezone
from django.conf import settings
import os
from .form import testf

def post_list(request):
    joueurs= Joueur.objects.all()
    equips = Equipement.objects.all()
    return render(request, 'blog/post_list.html', { 'joueurs':joueurs, 'equips':equips})

def formulaire(request):
    if request.method == 'POST':
        form = testf(request.POST, request.FILES)
        if form.is_valid():
            # Enregistrez le joueur dans la base de données
            form.save()
            print('ok') # Redirigez vers la page d'accueil ou une autre page après la création
    else:
        form = testf() 
        print("Formulaire non valide :")
    joueurs= Joueur.objects.all()
    equips = Equipement.objects.all()
    return render(request, 'blog/formulaire.html', { 'joueurs':joueurs, 'equips':equips, 'form':form})

def base(request):
    joueurs= Joueur.objects.all()
    equips = Equipement.objects.all()
    return render(request,'blog/base.html',{ 'joueurs':joueurs, 'equips':equips})


from .form import modifnom

def modif_joueur(request, numero):
    joueurs= Joueur.objects.all()
    equips = Equipement.objects.all()
    #joueur = Joueur.objects.get(Joueur, numero=numero)  
    joueur = get_object_or_404(Joueur, numero=numero) 
    if request.method == 'POST':
        form = modifnom(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            return redirect('page_accueil')  # Redirigez vers la page d'accueil ou une autre page après la modification
    else:
        form = modifnom(instance=joueur)

    return render(request, 'modifier_joueur.html', {'joueurs':joueurs, 'equips':equips,'form': form, 'joueur': joueur})




