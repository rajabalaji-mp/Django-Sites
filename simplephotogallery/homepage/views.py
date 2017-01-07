from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

# Create your views here.

def index(request):
    photos=Gallery.objects.all()
    context={'photos': photos}
    return render(request, 'homepage/index.html', context)