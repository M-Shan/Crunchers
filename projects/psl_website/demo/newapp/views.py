from django.shortcuts import render
from django.http import HttpResponse


def sentence(request):
    return HttpResponse('<H2>Welcome to the world of learning! </H2>')

# Create your views here.