from django.contrib import admin
from .models import Post 
#importanción relativa

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('__str__','actualizado', 'timestamp')
    #list_display_links = ["actualizado"] para que el link este en la fecha y no en el titulo
    list_filter = ['timestamp']
    search_fields = ['titulo', 'contenido']
    exclude = ('slug',)
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)