from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<H2>Welcome to News Feed Project from TechCrucnh! </H2>')

# Create your views here.
