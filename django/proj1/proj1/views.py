from email.policy import default
from shutil import register_unpack_format
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return render (request,'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    print (djtext)
    removepunc = request.GET.get('removepunc','off')
    print (removepunc)
    
    if removepunc =='on':
        punctuation_l = '''().,;[]'''
        analyzed_t = ''
        for charc in djtext:
            if charc not in punctuation_l:
                analyzed_t = analyzed_t + charc
         
        para = { 'purpose': 'remove punctions', 'analyzed_text': analyzed_t}
    
        return render (request, 'analyze.html', para)

    else:
        return HttpResponse ("error")

            
