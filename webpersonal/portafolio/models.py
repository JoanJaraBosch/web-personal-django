from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Títol')
    moreinfo = models.URLField(null=True, blank=True,verbose_name = 'Mes Informació')
    description = models.TextField(verbose_name = 'Desccripció')
    image = models.ImageField(verbose_name = 'Imatge', upload_to = 'projects')
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name = 'Data de creació')
    updatedDate = models.DateTimeField(auto_now=True, verbose_name = 'Data dactualització')

    class Meta:
        verbose_name = 'Projecte'
        verbose_name_plural = 'Projectes'
        ordering = ["-createdDate"]

    def __str__(self):
        return self.title