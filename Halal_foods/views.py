from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):

    return render(request, 'Halal_foods/home.html')


def lavash(request):
    foods = Foods.objects.all()
    context = {"foods": foods}
    return render(request, 'Halal_foods/lavash.html', context)


def ichmliklar(request):
    return render(request, 'Halal_foods/Ichmliklar.html')


def salatlar(request):
    return render(request, 'Halal_foods/Salatlar.html')


def ovqatlar(request):
    return render(request, 'Halal_foods/Ovqatlar.html')
