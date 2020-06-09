from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required




def home(request):
  return render (request, 'base.html')
