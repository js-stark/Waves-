from django.shortcuts import render

def home(request):

    return render(request,'index1.html')

def sponsers(request):

    return render(request,'gallery/gallery.html')
