# Generated by Django 5.0.1 on 2024-01-28 14:18

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0013_alter_emprunt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprunt',
            name='date',
            field=models.DateField(db_default=django.db.models.functions.datetime.Now()),
        ),
    ]
