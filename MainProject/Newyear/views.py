from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
now = datetime.datetime.now() 
day = now.day
month = now.month
year = now.year
def index(request):
    Newyear = (day == 14 and month == 2 and year == 2024)
    context = {'day':day, 
               'month':month, 
               'year': year,
               'Newyear' : Newyear
            }
    Newyear = (day == 14 and month == 2 and year == 2024)
    return render(request, 'Newyear/index.html',context)
