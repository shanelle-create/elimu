from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def table(request):
    return render(request,'table.html')

def form(request):
    return render(request,'form.html')


def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')