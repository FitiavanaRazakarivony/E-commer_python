

# traitement 

from django.shortcuts import render,redirect
#render mitady temple
from django.http import HttpResponse

from app.models import * 

from django.contrib.auth import login,authenticate, logout

# importation
# from .models import client
from .models import produit
# Create your views here.
def homeview(request):
    prd= produit.objects.all() 
    contexte = {'produit' : prd}
    
    return render(request, 'app/accueil.html', contexte)

def afficher(request, id):
    prd= produit.objects.all() 
    p = produit.objects.get(pk=id) #maka an le id produit sur client
    contexte = {'p' : p, 'produit' : prd}
    return render(request, 'app/accueil.html', contexte)

    # inscription
def inscription(request):
    return render(request, 'app/inscription.html', {})
    
def login(request):
    if request.method == 'POST':
        nomUt = request.POST.get("nomUt")
        mdp = request.POST.get("password")

        user = authenticate(username=nomUt,password=mdp)
        if user:
            login(request,user)
            return redirect('accueil')
        else:
            return HttpResponse('diso')

    return render(request, 'app/login.html', {})

def deconnexion(request):
    logout(request)
    return render(request, 'app/accueil.html', {})
    
# def listeclient(request):
    
#     clit= client.objects.all()
#     return render(request,'app/listeclient.html', {'client':clit})

    # return render(request, 'app/listeclient.html', {})
    
# -------------------- exp ----------
# def trt_inscription(request):
#     if request.method == 'POST':
#         nom = request.POST.get("nom")
#         prenom = request.POST.get("prenom")
#         adrs = request.POST.get("adress")
#         ville = request.POST.get("ville")
#         email = request.POST.get("email")
#         tel = request.POST.get("tel")
#         mdp = request.POST.get("mot_de_pass")
#         nomUt = request.POST.get("nomUt")
        
#         client.objects.create_user(last_name=nom, first_name=prenom,adrs=adrs,ville=ville,email=email,tel=tel,password=mdp,username=nomUt)
#     return render(request,'app/inscription.html', {})
# -------------------- fin exp ----------
# def AjoutProduitPanier(request,id):
#     if request.method == 'POST':
#         nom = request.POST.get("nomP")
#         prix = request.POST.get("prix")
#         desc = request.POST.get("desc")
#         id_prd = request.POST.get("id_prd")
#         id_client = client.objet.get(id)
#         qtt = request.POST.get("qtt")

#         mtt=prix*qtt
# # nom_produitPanier, qtt_produitPanier,prixUnit, mttt_Panier, description, id_client, id_produit

#         client.objects.create(nom_produitPanier=nom, qtt_produitPanier=qtt, prixUnit=prix,mttt_Panier=mtt, description=desc, id_client=id_client, id_produit=id_prd)
#     else:
#         return HttpResponse("tsy tafiditra")
#     return render(request,'app/inscription.html', {}) 
# # -------------------- panier ----------
# def panier(request,id):
#     p = produit.objects.get(pk=id) #maka an le id produit sur client
#     contexte = {'p' : p,}
#     return render(request, 'app/accueil.html', contexte)
# -------------------- fin panier ----------


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         



