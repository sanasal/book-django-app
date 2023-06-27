from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import Template , Context
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
from .models import Islam, Languages, Psychology
from .models import Mystry_and_Police,Programming, Science
from .models import Add_Comment , Report_Issue
from .models import Profile
from django.http import JsonResponse
import json  
from django.http import FileResponse
import os
from . import forms
from . import forms1

# Create your views here.

@csrf_protect


#manage home page 
def home(request):
    islams = Islam.objects.all()
    programmings = Programming.objects.all()
    sciences = Science.objects.all()
    mystrys = Mystry_and_Police.objects.all()
    psychologys= Psychology.objects.all()
    languages = Languages.objects.all()
    context = {'islams' : islams ,
      'programmings' : programmings ,
      'languages' : languages ,
      'mystrys' : mystrys,
      'psychologys' : psychologys,
      'sciences' : sciences}   
    return render(request, 'book.html' ,context)

#Go to Police Section
def police_view(request):
    mystrys = Mystry_and_Police.objects.all()
    context = {
      'mystrys' : mystrys,}   
    return render(request, 'police.html' , context)

#Go to Science Section
def Sciences_view(request):
    sciences = Science.objects.all()
    context = {
      'sciences' : sciences}   
    return render(request , 'sciences.html' , context)

#Go to Programming Section
def Programming_view(request):
    programmings = Programming.objects.all()
    context = {
      'programmings' : programmings ,}   
    return render(request , 'programming.html' , context)

#Go to Languages Section
def Languages_view(request):
    languages = Languages.objects.all()
    context = {
      'languages' : languages}   
    return render(request , 'languages.html' , context)

#Go to Islam Section
def Islam_view(request):
    islams = Islam.objects.all()
    context = {'islams' : islams }   
    return render(request , 'islam.html' , context)

#Go to Psychology Section
def Psychology_view(request):
    psychologys= Psychology.objects.all()
    context = {
      'psychologys' : psychologys}   
    return render(request , 'psychology.html' , context)      



#Give you book detail
@login_required(login_url='/log_in/')
def book_islam_detail(request, name):
    islam_books = Islam.objects.get(name = name)
    return render(request , 'book_islam_detail.html' , {'item' : islam_books}) 

@login_required(login_url='/log_in/')
def book_prog_detail(request, name):
    programming_books = Programming.objects.get(name = name)
    return render(request , 'book_prog_detail.html' , {'item' : programming_books})
 

@login_required(login_url='/log_in/')
def book_lang_detail(request, name):
    languages_books = Languages.objects.get(name = name)
    return render(request , 'book_lang_detail.html' , {'item' : languages_books}) 

@login_required(login_url='/log_in/')
def book_sci_detail(request, name):
    sciences_books = Sciences.objects.get(name = name)
    return render(request , 'book_sci_detail.html' , {'item' : sciences_books}) 

@login_required(login_url='/log_in/')
def book_psy_detail(request, name):
    psychology_books = Psychology.objects.get(name = name)
    return render(request , 'book_psy_detail.html' , {'item' : psychology_books}) 

@login_required(login_url='/log_in/')
def book_mystry_detail(request, name):
    mystry_books = Mystry_and_Police.objects.get(name = name)
    return render(request , 'book_mys_detail.html' , {'item' : mystry_books}) 



#Download pdf Files
def pdf(request , name):
    filepath = os.path.join('media', name)
    return FileResponse(open(filepath, 'rb'), content_type='book_shelf/pdf')
    


#search filters 
def Islam_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name' , None)
        if query_name:
            results = Islam.objects.filter(name= query_name)
            return render(request , 'islam.html' , {'results' : results})
        return render(request  , 'islam.html')


def prog_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name' , None)
        if query_name:
            results = Programming.objects.filter(name= query_name)
            return render(request , 'programming.html' , {'results' : results})
        return render(request  , 'programming.html')


def psy_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name' , None)
        if query_name:
            results = Psychology.objects.filter(name= query_name)
            return render(request , 'psychology.html' , {'results' : results})
        return render(request  , 'psychology.html')


def lang_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name' , None)
        if query_name:
            results = Languages.objects.filter(name= query_name)
            return render(request , 'languages.html' , {'results' : results})
        return render(request  , 'languages.html')


def police_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name' , None)
        if query_name:
            results = Mystry_and_Police.objects.filter(name= query_name)
            return render(request , 'police.html' , {'results' : results})
        return render(request  , 'police.html')


def sci_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name' , None)
        if query_name:
            results = Sciences.objects.filter(name= query_name)
            return render(request , 'sciences.html' , {'results' : results})
        return render(request  , 'sciences.html')


#Forms of add comment or report issue
@login_required(login_url='/log_in/')
def report_issue(request):
    if request.method == 'POST':
        form = forms1.Issue(request.POST)
        instance = form.save(commit = False)
        instance.writer = request.user
        instance.save()
        if form.is_valid():
            return redirect('book_shelf:home')

    else:
        form = forms1.Issue()
    return render(request, 'report_issue.html' ,{'form': form} )


@login_required(login_url='/log_in/')
def add_comment(request):
    comments = Add_Comment.objects.all()
    if request.method == 'POST':
        form = forms.Comment(request.POST)
        instance = form.save(commit = False)
        instance.writer = request.user
        instance.save()
        if form.is_valid():
            return redirect('book_shelf:add_comment')

    else:
        form = forms.Comment()
    return render(request, 'add_comment.html' ,{'form': form , 'comments':comments } )



#Sign in function
def sign_in(request):
    if request.method =='POST':   
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()              
            #log the user in
            login(request , user)           
            return redirect('book_shelf:home')
    else:           
       form = UserCreationForm()     
    return render(request, 'sign in.html' , {'form' : form})

#log in function
def log_in(request):
    if request.method == 'POST' :   
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            if 'next' in request.POST :
                return redirect(request.POST.get('next'))
            else: 
                return redirect ('book_shelf:home')
    else:
        form = AuthenticationForm()
    return render (request , 'log in.html' , {'form':form})


#Log out function
def log_out(request):
    if request.method == 'POST':
        logout(request)   
        return redirect ('book_shelf:home')