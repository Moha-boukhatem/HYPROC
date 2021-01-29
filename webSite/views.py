from django.shortcuts import render,HttpResponse
from .models import *
from .forms import *
def home(request):
    return render(request,'webSite/home.html')

def login(request):
    return render(request,'webSite/login.html')


def chefdepartement(request):
    return render(request,'webSite/chefdepartement.html')

def chefsection(request,pk):
   

    '''hah = userform()
    if request.method == "POST":
        hah=userform(request.POST)
        if hah.is_valid():
            hah.save()
    ''' 
    bb=utilisateur.objects.get(id=pk)
    modifier=userform(instance=bb)
    if request.method == "POST":
        modifier=userform(request.POST, instance=bb)
        if modifier.is_valid():
            modifier.save()
    
    return render(request,'webSite/chefsection.html',{'modifier':modifier})

def Utilisateur(request,pk):
    affiche=utilisateur.objects.get(id=pk)
    return render(request,'webSite/utilisateur.html',{'affiche':affiche})

def demandeTravail(request):
    return render(request,'webSite/demandeTravail.html')

def ordreTravail(request):
    return render(request,'webSite/ordreTravail.html')

def rapports(request):
    return render(request,'webSite/rapports.html')

def ouvriers(request):
    return render(request,'webSite/ouvriers.html')

def equipements(request):
    return render(request,'webSite/equipements.html')

def outillages(request):
    return render(request,'webSite/outillages.html')

    