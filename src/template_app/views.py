from django.shortcuts import render

def index_page(request):
    return render(request, 'home.html')

def list_page(request):
    return render(request, 'list.html')
