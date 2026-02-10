from rango.forms import CategoryForm, PageForm
from rango.models import Category, Page
from django.http import HttpRequest

from django.shortcuts import render, redirect
from django.urls import reverse

from typing import Any
from typing import TypedDict


class IndexContext(TypedDict):
    boldmessage: str
    categories: Any
    pages: Any


class PageContext(TypedDict):
    form: PageForm
    category: Category


# Create your views here.
def add_category(request: HttpRequest):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)

            return redirect("/rango/")
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request: HttpRequest, category_name_slug: str):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    
    # can't add page to a category if it doesn't exist :v
    if category is None:
        return redirect('/rango/')
    
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', 
                                        kwargs={'category_name_slug':
                                                category_name_slug}))
        else:
            print(form.errors)
    
    context_dict: PageContext = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)


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