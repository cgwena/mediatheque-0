from django.contrib import admin
from django.urls import path
import bibliothecaire.views
import membre.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bibliothecaire.views.home, name='home'),
    path('membres/', bibliothecaire.views.membres, name='membres'),
    path('membres/<int:id>/', bibliothecaire.views.membre_detail, name='membre_detail'),
    path('membres/add', bibliothecaire.views.membre_create, name='membre_create'),
    path('membres/<int:id>/update', bibliothecaire.views.membre_update, name='membre_update'),
    path('membre/<int:id>/delete', bibliothecaire.views.membre_delete, name='membre_delete')
]
