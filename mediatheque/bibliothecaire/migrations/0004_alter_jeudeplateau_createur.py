# Generated by Django 5.0.1 on 2024-01-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0003_jeudeplateau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeudeplateau',
            name='createur',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
