from django.contrib import admin

from .models import client, commande, details, produit
# Register your models here.
admin.site.register(client)
admin.site.register(commande)
admin.site.register(details)
admin.site.register(produit)

