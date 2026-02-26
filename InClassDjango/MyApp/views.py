from urllib import request, response
from django.shortcuts import render
from .models import teacher
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    teach = teacher.objects.all()

    return render(request, "MyApp/index.html",{'content': teach})