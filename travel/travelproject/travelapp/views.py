from django.http import HttpResponse
from django.shortcuts import render
from .models import place1
from . models import person


# Create your views here.
def demo(request):
    obj= place1.objects.all()
    objp = person.objects.all()
    return render(request, "index.html", {'result': obj, 'people': objp})
#    return render(request, "index.html", {'people': obj})
