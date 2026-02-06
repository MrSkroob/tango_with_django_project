from django.shortcuts import render
from rango.models import Category, Page
from django.http import HttpRequest

from typing import Any
from typing import TypedDict


class IndexContext(TypedDict):
    boldmessage: str
    categories: Any
    pages: Any


def show_category(request: HttpRequest, category_name_slug: str):
    context_dict: dict[str, Any] = {}

    try: 
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict["pages"] = pages
        context_dict["category"] = category
    except Category.DoesNotExist:
        context_dict["category"] = None
        context_dict["pages"] = None
    
    return render(request, 'rango/category.html', context=context_dict)


# Create your views here.
def index(request: HttpRequest):

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]


    context_dict: IndexContext = {
        "boldmessage": "Crunchy, creamy, cookie, candy, cupcake!",
        "categories": category_list,
        "pages": page_list
    }

    return render(request, "rango/index.html", context=context_dict)


def about(request: HttpRequest):
    context_dict = {
        "about_text": "here is the about page.",
    }
    return render(request, "rango/about.html", context=context_dict)