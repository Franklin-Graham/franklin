from django.shortcuts import render
from .models import *

# Create your views here.
def function(request):
    p = Profile.objects.all()
    db = Main.objects.all()
    return render(request,"index.html",{'img':db,'prof':p})