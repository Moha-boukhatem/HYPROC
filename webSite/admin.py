from django.contrib import admin

from .models import *

admin.site.register(chefdepartement)
admin.site.register(chefsection)
admin.site.register(utilisateur)
admin.site.register(section)
admin.site.register(ouvrier)
admin.site.register(outillage)
admin.site.register(equipement)
admin.site.register(localisation)
admin.site.register(demandeTravailChefSection)
admin.site.register(demandeTravailUtilisateur)
admin.site.register(ordreTravail)




