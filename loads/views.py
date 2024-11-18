from django.shortcuts import render
from django.views import generic
from .models import Load 

class LoadListView(generic.ListView):
    model = Load
    template_name = ".html"
