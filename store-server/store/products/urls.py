from django.urls import path

from products.views import products

app_name = 'products'

#Набор уникальных путей к именам файлов для перехода на отдельные страницы
urlpatterns = [
    path('', products, name='index')
]
