from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from travello.models import Destino
# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')              
    else:
        return render(request,'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordC = request.POST['passwordC'] 

        if passwordC == password:   
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                print('Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():        
                messages.info(request,'Email taken')
                print('Email taken')
                return redirect('register')
            else:    
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                messages.info(request,'User Created')
                print('User Created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching...')
            print('Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def logout (request):
    auth.logout(request)
    return redirect('/')


def createD (request):
    if request.method=='POST':
        name=request.POST['name']
        img=request.FILES['img']
        desc=request.POST['desc']
        price=request.POST['price']
        state=request.POST.get('state',True)
        offer=request.POST.get('offer',False)
        if Destino.objects.filter(name=name).exists():
            messages.info(request,'Name Taken')
            print('Name taken')
            return redirect('createD')
        else:
            if offer== 'on':
                offer=True
            else:
                offer=False
            if state== 'on':
                state=True
            else:
                state=False 
            imagenes=Destino.objects.create(name=name,img=img,desc=desc,price=price,offer=offer,state=state)    
            imagenes.save()
            print("Se añadio Destino correctamente")
            messages.info(request,'Destino añadido Correctamente')
            dests=Destino.objects.all()
            return redirect('/')   
    else:
        return render(request,'createD.html')
        

def listar(request):
    dests=Destino.objects.all()
    return render(request,'listar.html',{'dests':dests})
    
    
def delete(request, id):
    dest=Destino.objects.get(id=id)
    try:
        messages.info(request,dest.name+' Eliminado')    
        dest.delete()
    except:
        messages.info(request,'No se pudo eliminar el Objeto')
    return redirect('listar')


def actualizar(request,id):
    dest=Destino.objects.get(id=id)
    return render(request,"actualizar.html",{'dest':dest})

def modificar(request,id):
    dest=Destino.objects.get(id=id)
    if request.method=='POST':
        dest.name=request.POST['name']
        dest.img=request.FILES['img']
        dest.desc=request.POST['desc']
        dest.price=request.POST['price']
        offer=request.POST.get('offer')
        state=request.POST.get('state')
        if offer== 'on':
            dest.offer=True
        else:
            offer=False
        if state== 'on':
            dest.state=True
        else:
            state=False 
        dest.save()
        return redirect('listar')
    return render(request,"actualizar.html",{'dest':dest})
