from django.http import HttpResponse #importado

from django.shortcuts import render

# Create your views here.
def post_home(request):
    #return HttpResponse("<h1>Post home!</h1>")
    context = {
        "titulo": "Blog con Django"
    }
    return render(request, "index.html", context)