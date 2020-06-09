from django.shortcuts import render, redirect
from django.urls import path




def home(request):
  return render (request, 'base.html')
