# Generated by Django 4.2.7 on 2023-11-14 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_joueur_nom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joueur',
            name='etat',
        ),
        migrations.RemoveField(
            model_name='joueur',
            name='lieu',
        ),
        migrations.RemoveField(
            model_name='joueur',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='joueur',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='joueur',
            name='poste',
        ),
        migrations.RemoveField(
            model_name='joueur',
            name='taille',
        ),
    ]