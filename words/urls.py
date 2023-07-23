from django.urls import path

from . import views

urlpatterns = [
    # path("search", views.SearchView.as_view(), name="search"),
    path("", views.WordView.as_view(), name="list_words"),
]