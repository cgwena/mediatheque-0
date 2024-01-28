from django.contrib import admin
from django.urls import path
import bibliothecaire.views
import membre.views
import authentification.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentification.views.user_login, name="login"),
    path("logout/", authentification.views.logout_user, name="logout"),
    path("home", bibliothecaire.views.home, name="home"),
    path("membres/", bibliothecaire.views.membres, name="membres"),
    path("membres/<int:id>/", bibliothecaire.views.membre_detail, name="membre_detail"),
    path("membres/add", bibliothecaire.views.membre_create, name="membre_create"),
    path("membres/<int:id>/update",bibliothecaire.views.membre_update,name="membre_update"),
    path("membre/<int:id>/delete",bibliothecaire.views.membre_delete,name="membre_delete",),
    path("media/", bibliothecaire.views.media, name="media"),
    path("livre_detail/<int:id>/", bibliothecaire.views.livre_detail, name="livre_detail"),
    path("dvd_detail/<int:id>", bibliothecaire.views.dvd_detail, name="dvd_detail"),
    path("cd_detail/<int:id>/", bibliothecaire.views.cd_detail, name="cd_detail"),
    path("jeu_detail/<int:id>/", bibliothecaire.views.jeu_detail, name="jeu_detail"),
    path("livre/add", bibliothecaire.views.livre_create, name="livre_create"),
    path("dvd_create/", bibliothecaire.views.dvd_create, name="dvd_create"),
    path("cd_create/", bibliothecaire.views.cd_create, name="cd_create"),
    path("jeu_create/", bibliothecaire.views.jeu_create, name="jeu_create"),
    path("livre_update/<int:id>/", bibliothecaire.views.livre_update, name="livre_update"),
    path("dvd_update/<int:id>/", bibliothecaire.views.dvd_update, name="dvd_update"),
    path("cd_update/<int:id>/", bibliothecaire.views.cd_update, name="cd_update"),
    path("jeu_update/<int:id>/", bibliothecaire.views.jeu_update, name="jeu_update"),
    path("livre_delete/<int:id>/", bibliothecaire.views.livre_delete, name="livre_delete"),
    path("dvd_delete/<int:id>/", bibliothecaire.views.dvd_delete, name="dvd_delete"),
    path("cd_delete/<int:id>/", bibliothecaire.views.cd_delete, name="cd_delete"),
    path("jeu_delete/<int:id>/", bibliothecaire.views.jeu_delete, name="jeu_delete"),
    path('livre_emprunt/<int:id>', bibliothecaire.views.livre_emprunt, name='livre_emprunt'),
    path('dvd_emprunt/<int:id>', bibliothecaire.views.dvd_emprunt, name='dvd_emprunt'),
    path('cd_emprunt/<int:id>', bibliothecaire.views.cd_emprunt, name='cd_emprunt'),
    path('emprunt_impossible', bibliothecaire.views.emprunt_impossible, name='emprunt_impossible'),
    path('home_membres/', membre.views.home, name='membre_home')
]
