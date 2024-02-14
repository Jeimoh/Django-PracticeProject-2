from django.shortcuts import render
from django.http import HttpResponse


Tasks = ['Eat', 'code', '#sleep','nature walk','Repeat']
# Create your views here.
def index(request):
    context = {'Tasks': Tasks}
    return render(request, 'Tasks/index.html',context)
