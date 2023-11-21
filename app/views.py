from django.shortcuts import render

# Create your views here.
def ram(request):
    return render(request,'ram.html')

def sita(request):
    return render(request,'sita.html')

def ram2(request):
    return render(request,'ram2.html')