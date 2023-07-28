from django.http import HttpResponse
from django.shortcuts import render
from.models import services

# Create your views here.

def develop(request):
   obj = services.objects.all()
   return render(request,'index.html',{'result':obj})
#def demo(request):
 #  name = 'india'
  # return render(request,"home.html",{'obj':name})

#def about(request):
 #   return render(request,'about.html')
#def operations(request):
    #x = int(request.GET['num1'])
   # y = int(request.GET['num2'])
    #add = x+y
    #mul = x*y
    #div = x/y
    #sub = x-y
    #return render(request,'result.html',{'obj':add,'res':mul,'res1':div,'res2':sub})
