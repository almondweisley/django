from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h1> Landed home</h1>')


def about(request):
    return HttpResponse('<h2> Landed about</h2>')


def contact(request):
    return HttpResponse('<h3> Landed weisleyalmond@outlook.com</h3>')