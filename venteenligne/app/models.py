from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission, User

# Create your models here.
# ARTISTS = {
#     'francis-cabrel':{'name':'Francis Cabrel'},
#     'lej':{'name':'Elijay'},
#     'rosana':{'name':'Rosana'},
#     'rosana':{'name':'Rosana'},
#     'maria-dolore-pradera':{'name':'Maria Dolores Pradera'},
# }   

# ALBUMS = [
#     {'name': 'Sabine','artists':[ARTISTS['francis-cabrel']]},
#     {'name': 'La Dalle','artists':[ARTISTS['lej']]},
#     {'name': 'Luna nueva','artists':[ARTISTS['rosana'], ARTISTS['maria-dolore-pradera']]}
# ]


class client(AbstractUser):
    adrs = models.CharField(max_length = 200,null=False)
    ville = models.CharField(max_length = 200,null=False)
    tel = models.CharField(max_length = 200,null=False)
    groups = models.ManyToManyField(Group, related_name='client_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='client_user_permissions',
        blank=False,
    )
    
# class client(models.Model):
#     id_client = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length = 200,null=True)
#     prenom = models.CharField(max_length = 200,null=False)
#     adrs = models.CharField(max_length = 200,null=False)
#     ville = models.CharField(max_length = 200,null=False)
#     email = models.CharField(max_length = 200,null=False)
#     tel = models.CharField(max_length = 200,null=False)

class commande(models.Model):
    id_comm = models.AutoField(primary_key=True)
    date_com = models.DateTimeField(auto_now_add=True)
    mttt_total = models.CharField(max_length = 200,null=True)
    id_client = models.ForeignKey('client', on_delete=models.CASCADE)
    id_produit = models.ForeignKey('produit', on_delete=models.CASCADE) 
    nom_produit = models.CharField(max_length = 200,null=True)
    qtt_produit = models.CharField(max_length = 200,null=True)
    prixUnit = models.BooleanField(max_length = 200,null=True)
    description = models.CharField(max_length = 200,null=True)
    # article = models.ManyToManyField('Produit',through='details')



class Panier(models.Model):
    id_panier = models.AutoField(primary_key=True)
    date_Panier = models.DateTimeField(auto_now_add=True)
    nom_produitPanier = models.CharField(max_length = 200,null=True)
    qtt_produitPanier = models.CharField(max_length = 200,null=True)
    prixUnit = models.BooleanField(max_length = 200,null=True)
    mttt_Panier = models.CharField(max_length = 200,null=True)
    description = models.CharField(max_length = 200,null=True)
    id_client = models.ForeignKey('client', on_delete=models.CASCADE)
    id_produit = models.ForeignKey('produit', on_delete=models.CASCADE)
    # article = models.ManyToManyField('Produit',through='details')

class details(models.Model):
    id_comm = models.ForeignKey('commande', on_delete=models.PROTECT)
    id_produit = models.ForeignKey('produit', on_delete=models.PROTECT)
    qtt = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    class Meta:
        unique_together = [("id_comm","id_produit")]

class produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_prd = models.CharField(max_length = 200,null=True)
    description = models.CharField(max_length = 200,null=True)
    qtt_en_stock = models.CharField(max_length = 200,null=True)
    prixUnit = models.BooleanField(max_length = 200,null=True)    
    picture = models.ImageField(null=False,blank=False,upload_to="produit")

