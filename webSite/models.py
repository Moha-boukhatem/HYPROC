from django.db import models


class chefdepartement(models.Model):
    nom=models.CharField(max_length=50,null='true')
    prenom=models.CharField(max_length=50,null='true')
    mail=models.CharField(max_length=50,null='true')

    def __str__ (Self):
        return str(Self.nom) +" "+str(Self.prenom)


class section(models.Model):
    nom=models.CharField(max_length=50,null='true')    

    def __str__ (Self):
        return str(Self.nom)


class chefsection(models.Model):
    nom=models.CharField(max_length=50,null='true')
    prenom=models.CharField(max_length=50,null='true')
    mail=models.CharField(max_length=50,null='true')
    section=models.ForeignKey(section,null="true",on_delete=models.SET_NULL)

    def __str__ (Self):
        return str(Self.nom) +" "+str(Self.prenom)


class utilisateur(models.Model):
    nom=models.CharField(max_length=50,null='true')
    prenom=models.CharField(max_length=50,null='true')
    mail=models.CharField(max_length=50,null='true')
    section=models.ForeignKey(section,null="true",on_delete=models.SET_NULL)

    def __str__ (Self):
        return str(Self.nom) +" "+str(Self.prenom)


class ouvrier(models.Model):
    nom=models.CharField(max_length=50,null='true')
    prenom=models.CharField(max_length=50,null='true')
    disponible=models.BooleanField(default=False)
    section=models.ForeignKey(section,null="true",on_delete=models.SET_NULL)
    
    def __str__ (Self):
        return str(Self.nom)

class outillage(models.Model):
    nom=models.CharField(max_length=50,null='true')
    Quantité=models.IntegerField(null='true')



class localisation(models.Model):
    nom=models.CharField(max_length=50,null='true')

class equipement(models.Model):
    nom=models.CharField(max_length=50,null='true')
    localisation=models.ForeignKey(localisation,null="true",on_delete=models.SET_NULL)
    section=models.ForeignKey(section,null="true",on_delete=models.SET_NULL)
   
class demandeTravailChefSection(models.Model):
    description=models.CharField(max_length=50,null='true')
    date=models.DateTimeField(auto_now_add="true")
    chefsection=models.ForeignKey(chefsection,null="true",on_delete=models.SET_NULL)
    localisation=models.ForeignKey(localisation,null="true",on_delete=models.SET_NULL)


class demandeTravailUtilisateur(models.Model):
    description=models.CharField(max_length=50,null='true')
    date=models.DateTimeField(auto_now_add="true")
    utilisateur=models.ForeignKey(utilisateur,null="true",on_delete=models.SET_NULL)
    chefsection=models.ForeignKey(chefsection,null="true",on_delete=models.SET_NULL)
    

class ordreTravail(models.Model):
    description=models.CharField(max_length=500,null='true')
    date=models.DateTimeField(auto_now_add="true")
    ouvrier=models.ManyToManyField(ouvrier)
    outillage=models.ManyToManyField(outillage)
    section=models.ForeignKey(section,null="true",on_delete=models.SET_NULL)
    demandeTravailChefSection=models.ForeignKey(demandeTravailChefSection,null="true",on_delete=models.SET_NULL)
    demandeTravailUtilisateur=models.ForeignKey(demandeTravailUtilisateur,null="true",on_delete=models.SET_NULL)





    


