from django.contrib import admin
from .models import Batiment, Chambre, Etudiant
# Register your models here.
admin.site.register(Batiment)
admin.site.register(Chambre)
admin.site.register(Etudiant)