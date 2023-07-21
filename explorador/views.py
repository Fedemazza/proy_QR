#RECORDAR: User fedemazza Pass: 123f******
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages
from django.http import HttpResponse #FM
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
     form = CreateUserForm()
     if request.method == 'POST':
          #print('Printing POST', request.POST)
          form = CreateUserForm(request.POST)
          if form.is_valid():
               user = form.save()
               username = form.cleaned_data.get('username')

               group = Group.objects.get(name = 'user')
               user.groups.add(group)

               messages.success(request, 'Se creó la cuenta para: ' + username )
               return redirect('login')     

     context = {'form': form}
     return render(request, 'explorador/register.html', context)

@unauthenticated_user
def loginPage(request):

     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(request, username=username, password=password)

          if user is not None :
               login(request, user)
               return redirect('/')
          else:
               messages.info(request, 'Username or password is incorrect')
               return render(request, 'explorador/login.html')

     form = UserCreationForm()
     context = {'form': form}
     return render(request, 'explorador/login.html', context)

def logoutUser(request):
     logout(request)
     return redirect('login')

login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def userPage(request):
     context= {}
     return render(request, 'explorador/user.html', context)


login_required(login_url='login')
#@admin_only
def home(request):
     qrs = Qr.objects.all()
     users = User.objects.all()

     total_qrs = qrs.count()
     total_users = users.count()

     context = {'qrs': qrs, 'users': users, 'total_qrs': total_qrs, 'total_users': total_users}      
     return render(request, 'explorador/dashboard.html',context)

#login_required(login_url='login') --- Si comento este código no restrinjo a visitantes a ver los QR
#@allowed_users(allowed_roles=['admin'])
def qr(request,pk):
     try:
          qr = Qr.objects.get(serialnum=pk)
          cargas = Carga.objects.filter(qr=pk)
          qr_dict = Qr.objects.filter(serialnum=pk).values()
          context = {'qr': qr, 'qr_dict': qr_dict, 'cargas': cargas}
          url = 'explorador/qr.html'
     except:
          print('/crear_qr/'+pk)
          return redirect('/crear_qr/'+pk)
            
     return render(request, url, context)

login_required(login_url='login')
@allowed_users(allowed_roles=['admin','developer'])
def crearQr(request,pk):
     try:
          form = QrForm({'serialnum': pk, 'Creador': request.user})
     except:   
          form = QrForm({})
     if request.method == 'POST':
          form = QrForm(request.POST)          
          if form.is_valid():
               form.save()
               
               Carga(qr=form.instance, author=request.user).save()
               return redirect('/')
     


     context = {'form':form}
     return render(request, 'explorador/qr_form.html', context)

login_required(login_url='login')
@allowed_users(allowed_roles=['admin','developer'])
def updateQr(request,pk):
     qr = Qr.objects.get(serialnum=pk)
     if request.method == 'POST':
          #print('Printing POST', request.POST)
          form = QrForm(request.POST, instance=qr)
          if form.is_valid():
               form.save()
               Carga(qr=form.instance, author=request.user).save()
               return redirect('/')
     form = QrForm(instance=qr)
     context = {'form':form}
     return render(request, 'explorador/qr_form.html', context)

login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteQr(request,pk):
     qr = Qr.objects.get(serialnum=pk)
     if request.method == 'POST':
          qr.delete()
          return redirect('/')


     context = {'qr':qr}
     return render(request, 'explorador/delete.html', context)

