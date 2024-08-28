from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User

from users.forms import LoginUserForm, RegistrationUserForm
def login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginUserForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            form.save() #Сохраняем данные в БД
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = RegistrationUserForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)