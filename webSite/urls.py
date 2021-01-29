from django.urls import path
from . import views 

urlpatterns = [

    path('',views.home),

    path('login/',views.login,name='login'),

    path('chefdepartement/',views.chefdepartement,name='chefdepartement'),
    
    path('chefsection/<str:pk>',views.chefsection,name='chefsection'),
    
    path('utilisateur/<str:pk>',views.Utilisateur,name='utilisateur'),
    
    path('demandeTravail/',views.demandeTravail,name='demandeTravail'),
    
    path('ordreTravail/',views.ordreTravail,name='ordreTravail'),
    
    path('rapports/',views.rapports,name='rapports'),
    
    path('ouvriers/',views.ouvriers,name='ouvriers'),
    
    path('equipements/',views.equipements,name='equipements'),

    path('outillages/',views.outillages,name='outillages'),




]
