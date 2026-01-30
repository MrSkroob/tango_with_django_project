from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    context_dict = {
        "boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"
    }

    return render(request, "rango/index.html", context=context_dict)

def about(request: HttpRequest):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")