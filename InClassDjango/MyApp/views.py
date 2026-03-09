from urllib import request, response
from django.shortcuts import render
from .models import teacher
from django.http import HttpResponseRedirect

from .forms import  checkForm

# Create your views here.
def index(request):
    teach = teacher.objects.all()

    return render(request, "MyApp/index.html",{'content': teach})

def get_VET(request):
    if request.methord == 'POST':
        form = checkForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')