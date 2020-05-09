from django.urls import path

from . import views

# URL patterns for order app
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.addlocation, name="addlocation"),
    path("map/", views.map, name="map"),
]
