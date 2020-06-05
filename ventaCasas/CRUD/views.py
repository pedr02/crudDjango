from django.shortcuts import render, redirect
from CRUD.forms import houseForm, userForm
from CRUD.models import houses
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from CRUD.decorates import unauthenticated_user


def index(request):
    return render(request,'home')

@unauthenticated_user
def registerUser(request):
    form = userForm()
    if request.method=='POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render (request,'accounts/userRegister.html',context)

@unauthenticated_user
def loginUser(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            messages.info(request, 'Nombre o constraseña son incorrectos')
    context = {}
    return render(request, 'accounts/userLogin.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def houseCreate(request):
    if request.method == 'POST':
        form = houseForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Casa Agregada Correctamente!')
            return redirect ('list')
    else:
        form = houseForm()
    return render(request,'CRUD/HouseReg.html',{"form":form})   




class  modifyHouse(SuccessMessageMixin,LoginRequiredMixin , UpdateView):
    model = houses
    form_class = houseForm
    login_url = 'login'
    template_name = 'CRUD/houseReg.html'
    success_url = reverse_lazy('list')
    success_message = 'Casa Actualizada Correctamente!'

class viewHouse(LoginRequiredMixin,ListView):
    model = houses
    login_url = 'login'
    template_name = 'CRUD/index.html'

class detailHouse(LoginRequiredMixin,DetailView):
    model = houses
    login_url = 'login'
    template_name = 'CRUD/houseDetail.html'


class deleteHouse(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = houses
    
    login_url = 'login'
    def get_success_url(self): 
        success_message = 'Casa Eliminada Correctamente!' 
        messages.success (self.request, (success_message))       
        return reverse_lazy('list') 


