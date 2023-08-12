from django.urls import path
from . import views
app_name="movieapp"

urlpatterns = [
    path("",views.index,name="home"),
    path("movies/<int:movie_id>/",views.detail,name="details"),
    path("add/",views.add,name="added"),
    path("update/<int:id>/",views.update,name="edit"),
    path("delete/<int:id>",views.delete,name="remove")
]