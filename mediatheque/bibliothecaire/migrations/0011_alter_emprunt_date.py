# Generated by Django 5.0.1 on 2024-01-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0010_emprunt_emprunteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprunt',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]