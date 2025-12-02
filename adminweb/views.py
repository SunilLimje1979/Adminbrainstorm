from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import *

def WellCome(request):
    return HttpResponse('<h1 style="color:blue;">WellCome TO BrainStorm</h1>')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # POST request
    username = request.POST.get('uid')
    password = request.POST.get('password')
    print(username,password)
    # Check DB user
    user = TblUser.objects.filter(
        user_username=username,
        user_password=password
    ).first()

    if user:
        # SUCCESS LOGIN
        request.session['user_id'] = user.user_id
        request.session['user_name'] = user.user_firstname
        return redirect('dashboard')  # Change to your dashboard page

    else:
        # INVALID LOGIN
        messages.error(request, "Invalid Username or Password!")
        return render(request, 'login.html')

def logout(request):
    request.session.flush()  # clears all session data
    messages.success(request, "You have successfully signed out")
    return redirect('login')


def dashboard(request):
    return render(request, "dashboard.html")

# views.py
import re
from django.shortcuts import render
from .models import TblContent

def content(request):
    contents = TblContent.objects.filter(is_deleted=False).order_by('-content_id')

    def extract_youtube_id(url):
        if not url:
            return None
        patterns = [
            r"v=([^&]+)",             # watch?v=
            r"youtu\.be/([^?&]+)",    # youtu.be/abcd
            r"embed/([^?&]+)",        # embed/abcd
            r"shorts/([^?&]+)",       # shorts/abcd
        ]
        for p in patterns:
            m = re.search(p, url)
            if m:
                return m.group(1)
        return None

    for c in contents:
        c.embed_id = extract_youtube_id(c.content_url)

    return render(request, "content.html", {"contents": contents})
