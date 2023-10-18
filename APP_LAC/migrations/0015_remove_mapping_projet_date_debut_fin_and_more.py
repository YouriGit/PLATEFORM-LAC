# Generated by Django 4.2.4 on 2023-10-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_LAC', '0014_alter_suivi_de_indicateurs_projet_periode_execution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapping_projet',
            name='date_debut_fin',
        ),
        migrations.AddField(
            model_name='mapping_projet',
            name='date_de_fin_contrat',
            field=models.DateField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='mapping_projet',
            name='date_de_fin_essai',
            field=models.DateField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mapping_projet',
            name='date_debut_contrat',
            field=models.DateField(default=None, null=50),
        ),
        migrations.AlterField(
            model_name='mapping_projet',
            name='date_premiere_evaluation',
            field=models.DateField(default=None),
        ),
    ]