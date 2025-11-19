from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def WellCome(request):
    return HttpResponse('<h1 style="color:blue;">WellCome TO BrainStorm API APP</h1>')
