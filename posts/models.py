from django.db import models

from django.db import models
class Post(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    contenido = models.TextField()
    timestamp = models.TimeField(auto_now_add=True, auto_now=False)
    actualizado = models.TimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3 __str__
        return self.titulo

