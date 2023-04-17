from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from textblob import TextBlob
from newspaper import Article
from subprocess import run,PIPE 
import requests
import sys
import nltk

# Create your views here.
def index(request):
    context = {
        "variable1":"Ace is great",
        "variable2":"Vir is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def blogtext(request):
    return render(request, 'blogtext.html') 

def tpos(request):
    return render(request, 'tpos.html')     

def trans(request):
    return render(request, 'trans.html') 

def paraphrase(request):
    return render(request, 'paraphrase.html') 

def textspeech(request):
    return render(request, 'textspeech.html')     

def speechtext(request):
    return render(request, 'speechtext.html')      

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')

def test(request):
    return render(request, 'test.html')    

def senti(request):
    return render(request, 'senti.html')  
    
def keyw(request):
    return render(request, 'keyw.html')   

def keyf(request):
    return render(request, 'keyf.html')   

def publish(request):
    return render(request, 'publish.html')   

def subject(request):
    return render(request, 'subject.html') 

def spell(request):
    return render(request, 'spell.html') 

def pars(request):
    return render(request, 'pars.html') 

def dictonary(request):
    return render(request, 'dictonary.html') 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 


def external(request):
    inp= request.POST.get('param')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\test.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'test.html',{'data1':out.stdout})

def sentiment(request):
    inp= request.POST.get('but')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\sentiment_url.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'senti.html',{'data2':out.stdout})    

def keyword(request):
    inp= request.POST.get('key')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\keyword.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'keyw.html',{'data3':out.stdout})      

def date(request):
    inp= request.POST.get('date')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\date.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'publish.html',{'data4':out.stdout})  

def subj(request):
    inp= request.POST.get('subj')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\subj.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'subject.html',{'data5':out.stdout})

def txtcor(request):
    inp= request.POST.get('txtcor')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\txtcor.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'spell.html',{'data6':out.stdout})    

def parse(request):
    inp= request.POST.get('parse')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\parse.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'pars.html',{'data7':out.stdout})        

def txtsumm(request):
    inp= request.POST.get('txtsumm')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\txtsumm.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'test.html',{'data8':out.stdout})      

def txtkeyf(request):
    inp= request.POST.get('txtkeyf')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\txtkeyf.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'keyf.html',{'data9':out.stdout}) 

def sent(request):
    inp= request.POST.get('txtsentiment')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\txtsentiment.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'senti.html',{'data10':out.stdout}) 

def keyfurl(request):
    inp= request.POST.get('keyfurl')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\keyfurl.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'keyf.html',{'data11':out.stdout}) 

def wordkey(request):
    inp= request.POST.get('wordkey')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\wordkey.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'keyw.html',{'data12':out.stdout})  

def subjectivity(request):
    inp= request.POST.get('subjectivity')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\subjectivity.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'subject.html',{'data13':out.stdout}) 

def tts(request):
    inp= request.POST.get('tts')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\tts.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'textspeech.html',{'data14':out.stdout})     

def translate(request):
    inp= request.POST.get('translate')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\translate.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'trans.html',{'data15':out.stdout})

def para(request):
    inp= request.POST.get('para')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\para.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'paraphrase.html',{'data16':out.stdout})

def blog(request):
    inp= request.POST.get('blog')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\blog.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'blogtext.html',{'data17':out.stdout})

def stt(request):
    inp= request.POST.get('stt')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\stt.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'speechtext.html',{'data18':out.stdout})

def strans(request):
    inp= request.POST.get('strans')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\strans.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'trans.html',{'data19':out.stdout})        

def pos(request):
    inp= request.POST.get('pos')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\pos.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'tpos.html',{'data20':out.stdout})      

def dict(request):
    inp= request.POST.get('dict')
    out= run([sys.executable,'C:\\Users\\KABIR\\Desktop\\Hello\\home\\dict.py',inp],shell=False,stdout=PIPE, universal_newlines=True)
    print(out)
    return render(request,'dictonary.html',{'data21':out.stdout})   