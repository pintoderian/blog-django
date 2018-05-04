from django.db import models

from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.titulo
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

