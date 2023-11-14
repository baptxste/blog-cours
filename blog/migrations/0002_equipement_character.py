# Generated by Django 4.2.7 on 2023-11-12 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id_equip', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('disponibilite', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id_character', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('etat', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=200)),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.equipement')),
            ],
        ),
    ]
