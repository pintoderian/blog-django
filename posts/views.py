from django.http import HttpResponse #importado
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.
def post_home(request):
    #return HttpResponse("<h1>Post home!</h1>")
    query = Post.objects.all()
    paginator = Paginator(query, 4)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "titulo": "Blog con Django",
        "posts": posts
    }
    return render(request, "index.html", context)

def post_detail(request, slug=None):
    #return HttpResponse("<h1>Post home!</h1>")
    query = get_object_or_404(Post, slug=slug)
    context = {
        "titulo": query.titulo,
        "post": query
    }
    return render(request, "post.html", context)