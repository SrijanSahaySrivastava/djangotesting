from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello, Django! from about page")


def gaming(request):
    return HttpResponse("Hello, Django! gaming page")