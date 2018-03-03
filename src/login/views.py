from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from .forms import LoginForm
from django import forms

def loginView(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            return HttpResponseRedirect('/home')
    else:
        loginForm = LoginForm()
    return render(request,'login/login.html',{'loginform':loginForm})