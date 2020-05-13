from django.shortcuts import render
from . models import pythoncode
# Create your views here.

def index(request):
    return render(request, 'index.html')

def python(request):
    allrecord = pythoncode.objects.all()
    return render(request, 'python1.html',{'allrecord':allrecord})

def getpycode(request,id):
    allrecord = pythoncode.objects.all()
    info = pythoncode.objects.get(id=id)
    return render(request, 'getpycode.html',{'allrecord':allrecord,'info':info})