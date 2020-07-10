from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
                user.save();
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
    print('Add image')
    messages.info(request,'Add Destination')
    if request.method=='POST':
        name=request.POST['name']
        img=request.FILES['img']
        desc=request.POST['desc']
        price=request.POST['price']
        state=request.POST['state']
        offer=request.POST.get('offer',False)
        print(name+","+desc+","+price+","+state+","+offer)
        if User.objects.filter(name=name).exists():
            messages.info(request,'Ya exiten datos de esta Imagen')
            return redirect(createD)
        else:        
            if offer== 'on':
                offer=True
            else:
                offer=False
            if state== 'on':
                state=True
            else:
                state=False 
            print(name+","+desc+","+price+","+state+","+offer)       
            imagenes=Destino.objects.create(name=name,img=img,desc=desc,price=price,offer=offer)    
            imagenes.save();
            print("Se añadio Destino")
            messages.info(request,'Destino añadido')
            print('Destino añadido')
            return redirect('createD')
        dests=Destino.objects.all()
    else:
        return render(request,'createD.html')
def listar(request):
    data=Destination.objects.all()
    return render(request,'listar.html',{'data':data,})