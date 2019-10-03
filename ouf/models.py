from django.db import models
from django.conf import settings
from django.utils import timezone

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag    

class APropos(models.Model):
    titre = models.CharField(max_length=200)

    class Meta:
        verbose_name ='À Propos'
        verbose_name_plural ='À Propos'

    def __str__(self):
        return self.titre

class AProposSection(models.Model):
    a_propos = models.ForeignKey(APropos, on_delete=models.CASCADE)
    sous_titre = models.CharField(max_length=200)
    texte = models.TextField()

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return self.sous_titre

class ImageAPropos(models.Model):
    a_propos = models.ForeignKey(APropos, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to='uploaded_images/a_propos')
    legende = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.legende

class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True) # sélection manuelle de la date
    texte = models.TextField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Événement'
        verbose_name_plural ='Événements'

    def __str__(self):
        return self.titre

class ImageEvenement(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='images') # Many-to-One relation
    src = models.ImageField(upload_to='uploaded_images/evenements')
    legende = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.legende
