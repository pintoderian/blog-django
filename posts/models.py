from django.db import models

from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
class Post(models.Model):
    titulo = models.CharField(max_length=150)
    imagen = models.FileField(null=True,blank=True)
    slug = models.SlugField(unique=True)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.titulo
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-actualizado"]
#creando slug en el modelo
def create_slug(instance, new_slug=None):
    slug = slugify(instance.titulo)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)

