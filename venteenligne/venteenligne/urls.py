"""venteenligne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import *
# from app.views import *
from venteenligne import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeview , name="accueil"),
    path('..inscription/',homeview),
    path(' trt_inscription',trt_inscription,name="trt_inscription"),
    path(' AjoutProduitPanier',AjoutProduitPanier,name="ajoutProduitPanier"),
    path(' listeclient',listeclient,name="listeclient"),
    # path(' insertionProduit', insertionProduit,name="insertionProduit"),
    path('', homeview,name="home"),
    path('login/', login,name="login"),
    path('deconnexion/', deconnexion,name="deconnexion"),
    path('',homeview, name="homeview"),
    # Afficher pdt
    path('afficher/<int:id>', afficher, name='afficher')
    # path('panier', panier, name='panier')

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
