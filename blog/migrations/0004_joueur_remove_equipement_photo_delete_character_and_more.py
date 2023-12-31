# Generated by Django 4.2.7 on 2023-11-12 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_character_photo_alter_equipement_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('numero', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('etat', models.CharField(max_length=20)),
                ('poste', models.CharField(max_length=20)),
                ('taille', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipement',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
        migrations.AddField(
            model_name='joueur',
            name='lieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.equipement'),
        ),
    ]
