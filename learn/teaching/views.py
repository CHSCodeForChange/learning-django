from django.shortcuts import render, redirect
from teaching.models import Animal
from django.http import HttpResponse

# Create your views here.
def animal(request):
    animals = Animal.objects.all()
    #return HttpResponse("test")
    return render(request, 'teaching/animal.html', {'animal':animals})
