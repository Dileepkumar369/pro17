from django.shortcuts import render
from django.http import HttpResponse
def sam(request):
    return render(request,"sam.html")
def sam1(request):
    return render(request,"sam1.html")
# Create your views here.
