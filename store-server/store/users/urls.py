from django.urls import path

from users.views import login, register

app_name = 'users'

#Набор уникальных путей к именам файлов для перехода на отдельные страницы
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', register, name='register')
]