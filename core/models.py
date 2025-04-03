from django.db import models

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True)
    specialite = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Dr {self.prenom} {self.nom}"

class Commentaire(models.Model):
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name='commentaires')
    contenu = models.TextField()
    date = models.DateField(auto_now_add=True)
    source_origine = models.CharField(max_length=255, default="Inconnu")
    # note_global si besoin. Sinon, on peut le retirer.

    def __str__(self):
        return f"Commentaire #{self.pk} sur {self.medecin}"

class Aspect(models.Model):
    nom_aspect = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_aspect

POLARITE_CHOICES = [
    ('Positif', 'Positif'),
    ('Negatif', 'Negatif'),
   
]

class Aborder(models.Model):
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE)
    polarite = models.CharField(max_length=50, choices=POLARITE_CHOICES, blank=True)
    
    
    class Meta:
        unique_together = ('aspect',) 

    def __str__(self):
        return f"{self.commentaire} / {self.aspect} ({self.polarite})"
    
