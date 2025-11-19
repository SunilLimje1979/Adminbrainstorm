from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def WellCome(request):
    return HttpResponse('<h1 style="color:blue;">WellCome TO BrainStorm</h1>')


def login(request):
    if(request.method=='GET'):
        return render(request,'login.html')
    
    else:
        print(request.POST)
        username = request.POST.get('uid')
        password = request.POST.get('password')
        print(username,password)
        return redirect('login')
        # return HttpResponse("ok")