from django.shortcuts import render, redirect, get_object_or_404
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

# def content(request):
#     contents = TblContent.objects.filter(is_deleted=False).order_by('-content_id')

#     def extract_youtube_id(url):
#         if not url:
#             return None
#         patterns = [
#             r"v=([^&]+)",             # watch?v=
#             r"youtu\.be/([^?&]+)",    # youtu.be/abcd
#             r"embed/([^?&]+)",        # embed/abcd
#             r"shorts/([^?&]+)",       # shorts/abcd
#         ]
#         for p in patterns:
#             m = re.search(p, url)
#             if m:
#                 return m.group(1)
#         return None

#     for c in contents:
#         c.embed_id = extract_youtube_id(c.content_url)

#     return render(request, "content.html", {"contents": contents})
def content1(request):
    token = request.GET.get("token")
    contents = TblContent.objects.filter(is_deleted=False).order_by('-content_id')

    def extract_youtube_id(url):
        if not url:
            return None
        patterns = [
            r"v=([^&]+)",
            r"youtu\.be/([^?&]+)",
            r"embed/([^?&]+)",
            r"shorts/([^?&]+)",
        ]
        for p in patterns:
            m = re.search(p, url)
            if m:
                return m.group(1)
        return None

    auto_video_id = None  # for auto popup

    for c in contents:
        c.embed_id = extract_youtube_id(c.content_url)

        # Check token → auto popup video
        if token and c.content_code == token:
            auto_video_id = c.embed_id

    return render(request, "content1.html", {
        "contents": contents,
        "auto_video_id": auto_video_id,
        "invalid_token": token if token and not auto_video_id else None
    })

def content(request):
    token = request.GET.get("token")

    if not token:   # token missing
        return render(request, "content.html", {
            "video_title": "Video Not Available",
            "embed_id": None,
            "invalid": True
        })

    content = TblContent.objects.filter(content_code=token, is_deleted=False).first()

    if not content:  # token invalid
        return render(request, "content.html", {
            "video_title": "Video Not Available",
            "embed_id": None,
            "invalid": True
        })

    # extract YouTube ID
    def extract_youtube_id(url):
        if not url:
            return None
        patterns = [
            r"v=([^&]+)",
            r"youtu\.be/([^?&]+)",
            r"embed/([^?&]+)",
            r"shorts/([^?&]+)",
        ]
        for p in patterns:
            m = re.search(p, url)
            if m:
                return m.group(1)
        return None

    embed_id = extract_youtube_id(content.content_url)

    return render(request, "content.html", {
        "video_title": content.content_title,
        "embed_id": embed_id,
        "invalid": False
    })

################################## Content ###################################
############################ Add Content #########################################
def add_content(request):
    if request.method == "POST":
        try:
            content_type = request.POST.get("content_type")
            content_category = request.POST.get("content_category")
            content_title = request.POST.get("content_title")
            content_url = request.POST.get("content_url")
            content_code = request.POST.get("content_code")
            
            # Validation
            if not content_title:
                messages.error(request, "Content title is required.")
                return redirect("add_content")

            # Save record
            TblContent.objects.create(
                content_code=content_code,
                content_type=content_type,
                content_category=content_category,
                content_title=content_title,
                content_url=content_url,
                created_by=request.session.get("user_id", None),
            )

            messages.success(request, "Content added successfully!")
            return redirect("content_list")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    return render(request, "content/add_content.html")


def content_list(request):
    data = TblContent.objects.filter(is_deleted=False).order_by('-content_id')
    return render(request, "content/content_list.html", {"data": data})

def edit_content(request, id):
    content = get_object_or_404(TblContent, content_id=id)

    if request.method == "POST":
        content.content_code = request.POST.get("content_code")
        content.content_type = request.POST.get("content_type")
        content.content_category = request.POST.get("content_category")
        content.content_title = request.POST.get("content_title")
        content.content_url = request.POST.get("content_url")
        content.save()

        messages.success(request, "Content updated successfully!")
        return redirect("content_list")

    return render(request, "content/edit_content.html", {"content": content})

def delete_content(request, id):
    content = get_object_or_404(TblContent, content_id=id)
    content.is_deleted = True
    content.save()

    messages.success(request, "Content deleted successfully!")
    return redirect("content_list")
