"""Views for the main_app """
from django.shortcuts import render
from .models import Cat


def index(request):
    """ Passes cats as a dict to index """
    cats = Cat.objects.all()
    return render(request, "index.html", {"cats": cats})


def show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    render(request, "show.html", {"cat": cat})
