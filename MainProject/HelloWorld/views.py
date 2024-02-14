from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
    return render(request, 'HelloWorld/index.html')