from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Now


class User(AbstractUser):
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    nombreEmprunts = models.IntegerField(default=0)
    date_emprunts = models.DateField(null=True)


class Media(models.Model):
    name = models.fields.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Livre(Media):
    def __str__(self):
        return f"{self.name}"

    auteur = models.fields.CharField(max_length=100)


class Dvd(Media):
    def __str__(self):
        return f"{self.name}"

    realisateur = models.fields.CharField(max_length=100)


class Cd(Media):
    def __str__(self):
        return f"{self.name}"

    artiste = models.fields.CharField(max_length=100)


class JeuDePlateau(models.Model):
    def __str__(self):
        return f"{self.name}"

    name = models.fields.CharField(max_length=100)
    createur = models.fields.CharField(max_length=100, null=True)


class Emprunt(models.Model):
    date = models.DateField(db_default=Now())
    emprunteur = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
