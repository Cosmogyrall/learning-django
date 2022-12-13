# i have created this file - Yash
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request, 'index.html')

#def first(request):
 #   return HttpResponse('yash khairnar')

#def second(request):
    #return HttpResponse("I hope you are doing well")

#def text(request):
  #  f = open('/Users/yash/PycharmProjects/django_tuts/mysite/mysite/1.txt', 'r')
   # file_contents = f.read()
    #print(file_contents)
    #f.close()
    #return HttpResponse(file_contents, content_type='text/plain')

def analyze(request):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    djtext = request.POST.get('text', 'default')
    removepun = request.POST.get('box', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    charcount = request.POST.get('charcount','off')
    analyzed = ''
    #chart = djtext
    count = 0
    if removepun == 'on':
        for i in djtext:
            if i not in punctuations:
                analyzed += i
        #params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed }
        p = 'remove punctuation '
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        analyzed = djtext.upper()
        #params = {'purpose':'Upper case', 'analyzed_text':analyzed}
        djtext = analyzed
        p += 'and fullcaps '
        #return render(request, 'analyze.html',params)
    if charcount == 'on':
        for i in djtext:
            if i!="\n":
                count+=1
        print(count)
        p += 'and charcount'
        #params = {'purpose':'character counter', 'analyzed_text':count}
        #return render(request, 'analyze.html',params)
    #else:
     #  return HttpResponse('error')
    params = {'purpose':p , 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

#def home(request):    return HttpResponse("<h1>Home</h1>")

#def removepun(request):
