from django.shortcuts import render
from django.http import HttpResponse
from .models import Destino
# Create your views here.

def index(request):

    dests = Destino.objects.all() 

    return render(request,"index.html",{'dests':dests})