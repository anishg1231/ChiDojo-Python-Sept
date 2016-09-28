from django.shortcuts import render, HttpResponse
from .models import User,Quotes,Favorite
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.views import logout
from django.shortcuts import redirect
# Create your views here.

def login(request):
    result = User.objects.validateLogin(request)
    print(result)
    if result[0] == False:
        for message in result[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    request.session['user_id'] = result[1].id
    request.session['user_name'] = result[1].user_name
    return redirect('/quotes')

def register(request):
    result = User.objects.validateReg(request)
    print(result)
    if result[0] == False:
        for message in result[1]:
            messages.add_message(request, messages.ERROR, message)
    else:
        print result
        messages.add_message(request, messages.ERROR, 'Successful registered')
    return redirect('/')

###############################################################################
def index(request):
    return render(request, 'quotes/index.html')

def quotes(request):
    context ={
    'quote': Quotes.objects.all(),
    }
    print ("Way doesnt this work!")
    return render(request, 'quotes/quotes.html', context)

def new(request):
    return render(request,'quotes/quotes.html')

def create(request):
    if len(request.POST['quoted_by']) < 3:
        messages.add_message(request, messages.ERROR, 'Quoted by: More than 3 characters')
    if len(request.POST['message']) < 10:
        messages.add_message(request, messages.ERROR, 'Message: More than 10 characters')
        return redirect('/new')
    Quotes.objects.create(quoted_by=request.POST['quoted_by'], messages=request.POST['messages'], User_id= User.objects.get(id=request.session['user_id']) )
    return redirect('/quotes')

def logout(request):
    # logout(request)
    request.session.clear()
    return redirect('/')
