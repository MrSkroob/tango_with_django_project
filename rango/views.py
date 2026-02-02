from django.shortcuts import render
# from django.conf import settings
# from django.http import HttpResponse

from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    context_dict = {
        "boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"
    }

    return render(request, "rango/index.html", context=context_dict)

def about(request: HttpRequest):
    context_dict = {
        "about_text": "here is the about page.",
    }
    return render(request, "rango/about.html", context=context_dict)