# Generated by Django 4.2.4 on 2023-10-12 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_LAC', '0007_alter_mapping_projet_debut_recrutement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping_projet',
            name='debut_recrutement',
            field=models.DateField(default=datetime.datetime(2023, 10, 12, 23, 6, 3, 895881)),
        ),
        migrations.AlterField(
            model_name='mapping_projet',
            name='fin_recrutement',
            field=models.DateField(default=datetime.datetime(2023, 10, 12, 23, 6, 3, 895881)),
        ),
        migrations.AlterField(
            model_name='sous_activite_ap',
            name='contribution',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='sous_activite_ap',
            name='descapproche',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sous_activite_ap',
            name='inclusion_pers_besoin',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='sous_activite_ap',
            name='sousactivite',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sous_activite_ap',
            name='strategie_genre',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
