
# Create your views here.
from django.shortcuts import render,redirect
from django.core.validators import URLValidator
from django.core.files.base import ContentFile
from . import sentiment
def index(request):
    if (request.method == "POST"):
        data = request.POST.get('input')
        #m=Main.main(data)
        p=sentiment.pre(data)
        print(p[0])
        return render(request,'pro1/spider.html',{'pre':p[0],"con":p[1],'value':True,'sent':data})
        
    else:       
        return render(request, 'pro1/spider.html',{'error':False,"value":False})

def king(request):
    print("haha")
    return render(request, 'pro1/king.html')
