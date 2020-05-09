import json

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *

# Index view - return the home page
def index(request):
    # Send number of places entered in user is logged in
    if request.user.is_authenticated:
        places = Place.objects.filter(user=request.user).count
    else:
        places = 0
    return render(request, 'traceme/index.html', {"places": places})

# Addlocation view - add a location to lifemap
def addlocation(request):
    # GET - return page
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'traceme/addlocation.html', {"events": ["Born here", "Graduated here", "Other"]})
        else:
            return HttpResponse("You need to <a href=\"{% url 'login' %}\">login</a> or <a href=\"{% url 'register' %}\">register</a> to create a lifemap")
    # POST - save entry to database
    else:
        if request.user.is_authenticated:
            req = json.loads(request.body)
            place = Place(
                user=User.objects.filter(username=req["user"])[0],
                city=req["city"],
                state=req["state"],
                country=req["country"],
                latitude=req["latitude"],
                longitude=req["longitude"],
                start=req["start"],
                end=req["end"],
                reason=req["reason"],
                event=req["event"]
            )
            place.save()
            return HttpResponse("OK")
        else:
            return HttpResponse("You need to <a href=\"{% url 'login' %}\">login</a> or <a href=\"{% url 'register' %}\">register</a> to add items to your lifemap")

# Map view - return show lifemap
def map(request):
    if request.user.is_authenticated:
        context = {
            "place": [],
        }

        p = Place.objects.filter(user=request.user)
        for i in p:
            print(i.getinfo()["start"])
            context["place"].append(i.getinfo())

        return render(request, 'traceme/maps.html', context)
    else:
        return HttpResponse("You need to <a href=\"{% url 'login' %}\">login</a> or <a href=\"{% url 'register' %}\">register</a> to view your lifemap")
