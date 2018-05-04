from django.http import HttpResponse #importado

from django.shortcuts import render

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