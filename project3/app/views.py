from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('mr captain cool')
def virat(request):
    return HttpResponse('<h1>em cup namduuuuu</h1>')
def rohit(request):
    return HttpResponse('<h1><marquee>he is the world best open batsman</h1></marquee>')
