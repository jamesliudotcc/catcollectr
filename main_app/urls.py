from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cat_id>", views.show, name="show"),
    path("post_url/", views.post_cat, name="post_cat"),
]
