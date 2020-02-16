from django.shortcuts import render, redirect
from .models import Petshop
from .forms import PetshopForm

def welcome(request):
    return render(request, 'home.html', {'msg':'Hello World!'})

def Petshop_list(request):
    #list = PetShop.objects.all()
    #list = [x for x in list if x.available]
    context = {
        #"petshop":list,
        "petshop":Petshop.objects.all()
    }
    return render(request, 'list.html', context)


def Petshop_detail(request, pet_id):
    context = {
        "petshop": Petshop.objects.get(id=pet_id),
    }
    return render(request, 'detail.html', context)

def Petshop_create(request):
    form = PetshopForm()
    if request.method == "POST":
        form = PetshopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form
    }
    return render(request, 'create.html', context)

def Petshop_update(request, pet_id):
    obj = Petshop.objects.get(id= pet_id)
    form = PetshopForm(instance=obj)
    if request.method == "POST":
        form = PetshopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("pet-list")
    context = {

        "form":form,
        "obj":obj
    }
    return render(request, 'update.html', context)

def Petshop_delete(request, pet_id):

    Petshop.objects.get(id= pet_id).delete()
    return redirect("pet-list")
