from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index/index.html")

def gallery(request):
    return render(request, "index/gallery.html")
