"""Views for the main_app """
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Cat
from .forms import CatForm


def index(request):
    """ Passes cats as a dict to index """
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, "index.html", {"cats": cats, "form": form})


def show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, "show.html", {"cat": cat})


def post_cat(request):
    form = CatForm(request.POST)
    if form.is_valid:
        cat = form.save(commit=False)
        cat.save()
    return HttpResponseRedirect("/")
