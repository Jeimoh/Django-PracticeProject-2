from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
    return render(request, 'HelloWorld/index.html')
def HelloName(request,name):
    context = {'name':name.capitalize()}
    return render(request, 'HelloWorld/hello.html',context)