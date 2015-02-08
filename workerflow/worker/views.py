from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('worker:home')


def home(request):
    return render(request, 'home.html', {
        "request": request,
        })


def add(request):
    return render(request, 'add.html', {
        "request": request,
        })
