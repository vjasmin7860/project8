from django.shortcuts import render

# Create your views here.
def rings(request):
    return render(request,'rings.html')
