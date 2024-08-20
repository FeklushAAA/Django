from django.shortcuts import render

from users.models import User

from users.forms import LoginUserForm
def login(request):
    context = {'form': LoginUserForm()}
    return render(request, 'users/login.html', context)


def register(request):
    return render(request, 'users/register.html')