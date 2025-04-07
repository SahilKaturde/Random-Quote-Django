from django.shortcuts import render
from .models import Data
import random

# Create your views here.

def home(request):
    n = Data.objects.count()
    
    if n == 0:
        select_one = None
    else:
        random_index = random.randint(0, n - 1)
        select_one = Data.objects.all()[random_index]
    return render(request,'index.html',{'data':select_one})