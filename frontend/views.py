# Create your views here.
from django.conf.urls.defaults import *
from django.http import HttpResponse
#from django.template import Tempalte, Context
from django.shortcuts import render_to_response
from frontend.models import *
from frontend.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect



def index(request):
    user = request.user
    incidencias = DetalleIncidencia.objects.all()
    
    if user is not None and user.is_active:
        context= {"isLogin":True,'user':user,'incidencias':incidencias}
    else:
        context = {"isLogin":False,'incidencias':incidencias}
    return render_to_response('index.html',context) 

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            passwd= form.cleaned_data['password']
            user = authenticate(username=username, password=passwd)
            if user is not None:
                if user.is_active:
                    print "tu usuario esta activo . . ."
                    #logout(request)
                    login(request,user)
                    #login(
                    print "You provided a correct username and password!"
                    return HttpResponseRedirect('/')
                    #nombres = user.first_name +" "+ user.last_name   
                    #return render_to_response("pagina.html",{'user':nombres})
                else:
                    print "Your account has been disabled!"
            else:
                print "Your username and password were incorrect."            
        else:
            form = LoginForm()
            print "error"
    else:
        form = LoginForm()
        
    return render_to_response('login.html',{'form':form,}) 

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def pagina(request):
    context = {"user":request.user}
    return render_to_response('pagina.html',context)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print "form validado"
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            context={'success':True, 'username':form.cleaned_data['username']}
        else:
            print "form no validado"
            context = {'form':form, 'success':False}
    else:
        form = RegistroForm()
        context = {'form':form, 'success':False}
    return render_to_response('registro.html',context)
