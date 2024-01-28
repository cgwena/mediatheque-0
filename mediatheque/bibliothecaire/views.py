from django.shortcuts import render, redirect
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)

# Custom function to check if the user has is_staff set to True


from bibliothecaire.models import User, Livre, Dvd, Cd, JeuDePlateau, Emprunt
from bibliothecaire.forms import (
    MembreForm,
    LivreForm,
    DvdForm,
    CdForm,
    JeuForm,
    EmpruntForm,
)


def is_staff_user(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_staff_user)
def home(request):
    return render(request, "bibliothecaire/home.html")


@login_required
@user_passes_test(is_staff_user)
def membres(request):
    membres = User.objects.all()
    return render(request, "bibliothecaire/membres.html", {"membres": membres})


@login_required
@user_passes_test(is_staff_user)
def membre_detail(request, id):
    membre = User.objects.get(id=id)
    return render(request, "bibliothecaire/membre_detail.html", {"membre": membre})


@login_required
@user_passes_test(is_staff_user)
def membre_create(request):
    if request.method == "POST":
        form = MembreForm(request.POST)
        if form.is_valid():
            membre = form.save(commit=False)
            membre.set_password(form.cleaned_data["password"])
            membre.save()
    else:
        form = MembreForm()
    return render(request, "bibliothecaire/membre_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def membre_update(request, id):
    membre = User.objects.get(id=id)
    if request.method == "POST":
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect("membre_detail", membre.id)
    else:
        form = MembreForm(instance=membre)
    return render(request, "bibliothecaire/membre_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def membre_delete(request, id):
    membre = User.objects.get(id=id)
    if request.method == "POST":
        membre.delete()
        return redirect("membres")
    return render(request, "bibliothecaire/membre_delete.html", {"membre": membre})


@login_required
@user_passes_test(is_staff_user)
def media(request):
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(
        request,
        "bibliothecaire/media.html",
        {"livres": livres, "dvds": dvds, "cds": cds, "jeux": jeux},
    )


@login_required
@user_passes_test(is_staff_user)
def livre_detail(request, id):
    livre = Livre.objects.get(id=id)
    return render(request, "bibliothecaire/livre_detail.html", {"livre": livre})


@login_required
@user_passes_test(is_staff_user)
def dvd_detail(request, id):
    dvd = Dvd.objects.get(id=id)
    return render(request, "bibliothecaire/dvd_detail.html", {"dvd": dvd})


@login_required
@user_passes_test(is_staff_user)
def cd_detail(request, id):
    cd = Cd.objects.get(id=id)
    return render(request, "bibliothecaire/cd_detail.html", {"cd": cd})


@login_required
@user_passes_test(is_staff_user)
def jeu_detail(request, id):
    jeu = JeuDePlateau.objects.get(id=id)
    return render(request, "bibliothecaire/jeu_detail.html", {"jeu": jeu})


@login_required
@user_passes_test(is_staff_user)
def livre_create(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save()
            return redirect("livre_detail", livre.id)
    else:
        form = LivreForm()
    return render(request, "bibliothecaire/media_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def dvd_create(request):
    if request.method == "POST":
        form = DvdForm(request.POST)
        if form.is_valid():
            dvd = form.save()
            return redirect("dvd_detail", dvd.id)
    else:
        form = DvdForm()
    return render(request, "bibliothecaire/media_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def cd_create(request):
    if request.method == "POST":
        form = CdForm(request.POST)
        if form.is_valid():
            cd = form.save()
            return redirect("cd_detail", cd.id)
    else:
        form = CdForm()
    return render(request, "bibliothecaire/media_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def jeu_create(request):
    if request.method == "POST":
        form = JeuForm(request.POST)
        if form.is_valid():
            jeu = form.save()
            return redirect("jeu_detail", jeu.id)
    else:
        form = JeuForm()
    return render(request, "bibliothecaire/media_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def livre_update(request, id):
    livre = Livre.objects.get(id=id)
    if request.method == "POST":
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect("livre_detail", livre.id)
    else:
        form = LivreForm(instance=livre)
    return render(request, "bibliothecaire/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def dvd_update(request, id):
    dvd = Dvd.objects.get(id=id)
    if request.method == "POST":
        form = DvdForm(request.POST, instance=dvd)
        if form.is_valid():
            form.save()
            return redirect("dvd_detail", dvd.id)
    else:
        form = DvdForm(instance=dvd)
    return render(request, "bibliothecaire/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def cd_update(request, id):
    cd = Cd.objects.get(id=id)
    if request.method == "POST":
        form = CdForm(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            return redirect("cd_detail", cd.id)
    else:
        form = CdForm(instance=cd)
    return render(request, "bibliothecaire/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def jeu_update(request, id):
    jeu = JeuDePlateau.objects.get(id=id)
    if request.method == "POST":
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
            return redirect("jeu_detail", jeu.id)
    else:
        form = JeuForm(instance=jeu)
    return render(request, "bibliothecaire/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def livre_delete(request, id):
    livre = Livre.objects.get(id=id)
    if request.method == "POST":
        livre.delete()
        return redirect("media")
    return render(request, "bibliothecaire/media_delete.html", {"media": livre})


@login_required
@user_passes_test(is_staff_user)
def dvd_delete(request, id):
    dvd = Dvd.objects.get(id=id)
    if request.method == "POST":
        dvd.delete()
        return redirect("media")
    return render(request, "bibliothecaire/media_delete.html", {"media": dvd})


@login_required
@user_passes_test(is_staff_user)
def cd_delete(request, id):
    cd = Cd.objects.get(id=id)
    if request.method == "POST":
        cd.delete()
        return redirect("media")
    return render(request, "bibliothecaire/media_delete.html", {"media": cd})


@login_required
@user_passes_test(is_staff_user)
def jeu_delete(request, id):
    jeu = JeuDePlateau.objects.get(id=id)
    if request.method == "POST":
        jeu.delete()
        return redirect("media")
    return render(request, "bibliothecaire/media_delete.html", {"media": jeu})


@login_required
@user_passes_test(is_staff_user)
def livre_emprunt(request, id):
    livre = Livre.objects.get(id=id)
    emprunt = Emprunt.objects.all()
    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if livre.disponible == True:
            emprunt = form.save()
            user = User.objects.get(id=emprunt.emprunteur.id)
            if user.nombreEmprunts >= 3:
                return redirect("emprunt_impossible")
            else:
                livre.disponible = False
                livre.save()
                user.nombreEmprunts += 1
                user.save()
                return redirect("livre_detail", livre.id)
        elif livre.disponible == False:
            livre.disponible = True
            livre.save()
            emprunt = form.save()
            user = User.objects.get(id=emprunt.emprunteur.id)
            user.nombreEmprunts -= 1
            user.save()
            return redirect("livre_detail", livre.id)
    form = EmpruntForm()
    return render(
        request, "bibliothecaire/media_emprunt.html", {"media": livre, "form": form}
    )


@login_required
@user_passes_test(is_staff_user)
def dvd_emprunt(request, id):
    dvd = Dvd.objects.get(id=id)
    emprunt = Emprunt.objects.all()
    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if dvd.disponible == True:
            emprunt = form.save()
            user = User.objects.get(id=emprunt.emprunteur.id)
            if user.nombreEmprunts >= 3:
                return redirect("emprunt_impossible")
            else:
                dvd.disponible = False
                dvd.save()
                user.nombreEmprunts += 1
                user.save()
                return redirect("dvd_detail", dvd.id)
        elif dvd.disponible == False:
            dvd.disponible = True
            dvd.save()
            emprunt = form.save()
            user = User.objects.get(id=emprunt.emprunteur.id)
            user.nombreEmprunts -= 1
            user.save()
            return redirect("dvd_detail", dvd.id)
    form = EmpruntForm()
    return render(
        request, "bibliothecaire/media_emprunt.html", {"media": dvd, "form": form}
    )


@login_required
@user_passes_test(is_staff_user)
def cd_emprunt(request, id):
    cd = Cd.objects.get(id=id)
    emprunt = Emprunt.objects.all()
    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if cd.disponible == True:
            emprunt = form.save()
            user = User.objects.get(id=emprunt.emprunteur.id)
            if user.nombreEmprunts >= 3:
                return redirect("emprunt_impossible")
            else:
                cd.disponible = False
                cd.save()
                user.nombreEmprunts += 1
                user.save()
                return redirect("cd_detail", cd.id)
        elif cd.disponible == False:
            cd.disponible = True
            cd.save()
            emprunt = form.save()
            user = User.objects.get(id=emprunt.emprunteur.id)
            user.nombreEmprunts -= 1
            user.save()
            return redirect("cd_detail", cd.id)
    form = EmpruntForm()
    return render(
        request, "bibliothecaire/media_emprunt.html", {"media": cd, "form": form}
    )


@login_required
@user_passes_test(is_staff_user)
def emprunt_impossible(request):
    return render(request, "bibliothecaire/emprunt_impossible.html")
