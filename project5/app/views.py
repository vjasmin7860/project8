from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(reuest):
    return HttpResponse('this is string formate')
def jasmin(request):
    return render(request,'jasmin.html')
