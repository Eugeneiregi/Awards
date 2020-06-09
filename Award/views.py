from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *




def home(request):
  current_user = request.user
  project_images = Project.fetch_all_images()
  image_params = {
    'all_images':project_images,
    'current': current_user,
  }
  return render (request, 'base.html')
  return render(request, "main/index.html", image_params)



def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Project.objects.all()
        print(posts)
    except Project.DoesNotExist:
        posts = None
    return render(request, 'main/index.html', {'posts': posts, 'form': form})





    def signup(request):
    global register_form
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
        register_form = {
            'form': form,
        }
    return render(request, 'registration/signup.html', {'form': form})
