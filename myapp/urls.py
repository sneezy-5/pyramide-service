from django.urls import path

from . import views

urlpatterns = [
    path('', views.acceuil, name= "acceuils"),
    path('activite/', views.activite, name= "activites"),
    path('contact/', views.contact, name= "contacts"),
    path('electricite-general/', views.electricite, name= "electricite"),
    path('batiment/', views.batiment, name= "batiments"),
    path('plombier/', views.plombier, name= "plombiers"),
    path('maintenance/', views.maintenance, name= "maintenances"),
    path('vente/', views.vente ,name= "ventes"),

]
