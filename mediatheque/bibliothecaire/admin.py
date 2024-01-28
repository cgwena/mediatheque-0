from django.contrib import admin

from bibliothecaire.models import User, Livre, Dvd, Cd, JeuDePlateau, Emprunt

admin.site.register(User)
admin.site.register(Livre)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(JeuDePlateau)
admin.site.register(Emprunt)
