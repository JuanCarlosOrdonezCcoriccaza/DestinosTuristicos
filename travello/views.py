from django.shortcuts import render
from django.http import HttpResponse
from .models import Destino
# Create your views here.

def index(request):

    dest1 =  Destino()
    dest1.name='Munbai'
    dest1.desc='New city,excelent for a traveling '
    dest1.img='destination_1.jpg'
    dest1.price= 699.99
    dest1.offer= True

    dest2 =  Destino()
    dest2.name='Mancora-Peru'
    dest2.desc='Turisc travel , then your want travel to a  Mancora in Perú'
    dest2.img='destination_8.jpg'
    dest2.price= 499.99
    dest2.offer= True

    dest3 =  Destino()
    dest3.name='New York'
    dest3.desc='City for traveling '
    dest3.img='destination_3.jpg'
    dest3.price= 899.99
    dest3.offer=False

    dests= [dest1,dest2,dest3]
    return render(request,"index.html",{'dests':dests})