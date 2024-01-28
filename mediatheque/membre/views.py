from django.shortcuts import render
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(
        request,
        "membre/home.html",
        {"livres": livres, "dvds": dvds, "cds": cds, "jeux": jeux},
    )
