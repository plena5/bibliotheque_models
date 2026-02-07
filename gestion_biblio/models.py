from django.db import models
from django .contrib.auth.models import User

# Create your models here.
class Habitant(models.Model):
    id=models.BigAutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_naissance=models.DateField()
    CNI=models.CharField(max_length=20,unique=True)
    adresse=models.CharField (max_length=100)
    ville=models.CharField (max_length=20)
    telephone=models.CharField (max_length=20)
    email=models.EmailField()
    date_inscription=models.DateField(auto_now_add=True)
    actif=models.BooleanField(default=True)
    amende=models.DecimalField(max_digits=8,decimal_places=2,default= 0)
    def __str__(self):
        return f"{self.user.username}"

class Categorie(models.Model):
    id=models.BigAutoField(primary_key=True)
    nom=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom}"

    
    
class Ouvrage(models.Model):
    
    ETAT = [
        ('neuf', 'Neuf'),
        ('bon', 'Bon etat'),
        ('abime', 'Abime'),
    ]
    id=models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20, blank=True, null=True,unique=True)
    annee_publication = models.IntegerField()
    nombre_pages = models.IntegerField()
    langue = models.CharField(max_length=50)
    etat = models.CharField(max_length=10, choices=ETAT, default='bon')
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateField(auto_now_add=True)
    categorie=models.ForeignKey(Categorie,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.titre} ({self.code})"
    
    
class Emprunt(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('retourne', 'Retourne'),
        ('retard', 'En retard'),
    ]
    id=models.BigAutoField(primary_key=True)
    emprunteur = models.ForeignKey(Habitant, on_delete=models.PROTECT, related_name='emprunts')
    livre = models.ForeignKey(Ouvrage, on_delete=models.PROTECT, related_name='emprunts')
    date_emprunt = models.DateField(auto_now_add=True)
    date_limite_retour = models.DateField()
    date_reel_retour = models.DateField(blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
    amende = models.DecimalField(max_digits=8, decimal_places=2, default=0)


    def __str__(self):
        return f"{self.emprunteur} {self.livre}"


    
    
    




