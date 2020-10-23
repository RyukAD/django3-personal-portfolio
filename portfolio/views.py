from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    ctx = {'projects': projects}
    return render(request, 'portfolio/home.html', ctx)

