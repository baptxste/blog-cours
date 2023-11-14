# Generated by Django 4.2.7 on 2023-11-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_equipement_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='photo',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Billet',
        ),
    ]
