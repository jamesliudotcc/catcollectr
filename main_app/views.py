"""Views for the main_app """
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .models import Cat, User
from .forms import CatForm, LoginForm


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
        cat.user = request.user
        cat.save()
    return HttpResponseRedirect("/")


def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, "profile.html", {"username": username, "cats": cats})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    print("The account has been disabled")
            else:
                print("The login credentials are incorrect")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def like_cat(request):
    cat_id = request.GET.get("cat_id", None)

    likes = 0
    if cat_id:
        cat = Cat.objects.get(id=int(cat_id))
        if cat is not None:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()
    return HttpResponse(likes)
