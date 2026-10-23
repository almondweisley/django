from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.htm')


def contact(request):
    return HttpResponse('<h3> Landed weisleyalmond@outlook.com</h3>')