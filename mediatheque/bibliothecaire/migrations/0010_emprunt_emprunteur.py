# Generated by Django 5.0.1 on 2024-01-27 21:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0009_emprunt_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='emprunteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]