from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    biographie = models.TextField()

    def __str__(self):
        return self.nom, self.prenom, self.biographie
    
class LivreAudio(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    description = models.TextField()
    duree = models.IntegerField() # en secondes
    chemin_fichier = models.FileField(upload_to='livres_audio/')

    def __str__(self):
        return self.titre, self.auteur, self.description, self.duree