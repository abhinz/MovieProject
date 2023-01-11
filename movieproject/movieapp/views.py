from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from . forms import movieform
# Create your views here.

def index(request,):
    movi=movie.objects.all()
    context={
        'movielist':movi

    }
    return render(request,"index.html",context)

def details(request,movi_id):
    movi=movie.objects.get(id=movi_id)
    return render(request,'details.html',{'movie':movi})

def addmovie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        move=movie(name=name,desc=desc,year=year,img=img)
        move.save()
    return render(request,'add.html')

def update(request,id):
    mov=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':mov})

def delete(request,id):
    if request.method=='POST':
        movi=movie.objects.get(id=id)
        movi.delete()
        return redirect('/')
    return render(request,'delete.html')