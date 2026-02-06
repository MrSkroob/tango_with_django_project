from django.shortcuts import render
from rango.models import Category
from django.http import HttpRequest

from typing import Any
from typing import TypedDict


class IndexContext(TypedDict):
    boldmessage: str
    categories: Any


# Create your views here.
def index(request: HttpRequest):

    category_list = Category.objects.order_by('-likes')[:5]


    context_dict: IndexContext = {
        "boldmessage": "Crunchy, creamy, cookie, candy, cupcake!",
        "categories": category_list
    }

    return render(request, "rango/index.html", context=context_dict)

def about(request: HttpRequest):
    context_dict = {
        "about_text": "here is the about page.",
    }
    return render(request, "rango/about.html", context=context_dict)