from django.shortcuts import render, HttpResponse, redirect
from dojo_app.models import Dojo, Ninja

def index(request):
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()

    context = {
        'dojos': dojos,
        'ninjas': ninjas
    }
    return render(request, 'index.html', context)

def form_dojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
    d = Dojo.objects.create(name = name, city = city, state = state)
    d.save()
    return redirect('/')

def form_ninja(request): 
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        dojo = Dojo.objects.get(id = request.POST['id'])
    n = Ninja.objects.create(first_name = fname, last_name = lname, dojo = dojo)
    n.save()
    return redirect('/')

def dojo_remove(request):
    if request.method == 'POST':
        remove = request.POST['remove']
    d = Dojo.objects.get(id=remove)
    d.delete()
    return redirect('/')