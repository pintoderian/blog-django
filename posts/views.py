from django.http import HttpResponse #importado

from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.
def post_home(request):
    #return HttpResponse("<h1>Post home!</h1>")
    query = Post.objects.all()
    context = {
        "titulo": "Blog con Django",
        "posts": query
    }
    return render(request, "index.html", context)

def post_detail(request, id=None):
    #return HttpResponse("<h1>Post home!</h1>")
    query = get_object_or_404(Post, id=id)
    context = {
        "titulo": "Detalle del post",
        "post": query
    }
    return render(request, "post.html", context)