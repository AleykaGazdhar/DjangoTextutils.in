from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail  # function we will use to send email
from django.conf import settings

def home(request):
    return render(request, 'home.html', {})  # render is used to deploy templates(html files)

def analyze(request):
    djtext= request.POST.get('text','default') #get the text

    # Check Switch values
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    extraspaceremover= request.POST.get('extraspaceremover','off')
    charcount= request.POST.get('charcount','off')

    #check which Switch is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>.?/@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed= analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == 'on'):
        analyzed = len(djtext)
        params = {'purpose': 'Count Number of Characters', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps !='on' and extraspaceremover != 'on' and newlineremover!='on' and charcount != 'on'):
        return render(request, 'nooperation.html', {})
    
    return render(request, 'analyze.html', params)

def nooperation(request):
    return render(request, 'nooperation.html', {})


def about(request):
    return render(request, 'about.html', {})

def contact(request):
    # logic for sending email
    if request.method == "POST":
        # get data from the form
        name = request.POST.get('Full-Name')
        email = request.POST.get('Email-Address')
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')
        send_mail(
            subject,  #subject
            message,  #message
            email,    # from email
            ['aleykagazdhar1601@gmail.com'],  # to email
            fail_silently=False,
        )
        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})




