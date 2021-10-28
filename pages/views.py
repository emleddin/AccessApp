from django.shortcuts import render

from django.http import HttpResponse

def home_page_view(request):
    return render(request, 'map.html', {})

def default_map(request):
    return render(request, 'map.html', {})