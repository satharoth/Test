from django.shortcuts import render,redirect
from .models import Libreria

# Create your views here.

def inicio(request):
    libreria = Libreria.objects.all()
    return render(request,"libreria.html",{"libros": libreria})

def registarlibros(request):
    Libro = request.POST['Libro']
    Autor = request.POST['Autor']
    Editorial = request.POST['Editorial']    
    libros=Libreria.objects.create(Libro=Libro, Autor=Autor, Editorial=Editorial)
    return redirect('/')

def edicionlibros(request,ID):    
    libros=Libreria.objects.get(ID=ID)
    return render(request,"edicionlibros.html",{"libros": libros})

def editarlibros(request):
    IDLi = request.POST['ID']
    Libro = request.POST['Libro']
    Autor = request.POST['Autor']
    Editorial = request.POST['Editorial']  
        
    libros=Libreria.objects.get(ID=IDLi)
    libros.Libro=Libro  
    libros.Autor=Autor 
    libros.Editorial=Editorial 
    libros.save()
    return redirect('/')

def eliminarlibros(request,ID):    
    libros=Libreria.objects.get(ID=ID)
    libros.delete()
    return redirect('/')