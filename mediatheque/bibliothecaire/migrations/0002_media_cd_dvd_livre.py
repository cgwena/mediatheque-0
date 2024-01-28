# Generated by Django 5.0.1 on 2024-01-27 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('emprunteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliothecaire.media')),
                ('artiste', models.CharField(max_length=100)),
            ],
            bases=('bibliothecaire.media',),
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliothecaire.media')),
                ('realisateur', models.CharField(max_length=100)),
            ],
            bases=('bibliothecaire.media',),
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliothecaire.media')),
                ('auteur', models.CharField(max_length=100)),
            ],
            bases=('bibliothecaire.media',),
        ),
    ]