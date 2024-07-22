
from django.contrib import admin
from django.urls import path

from products.views import index, products

#Набор уникальных путей к именам файлов для перехода на отдельные страницы
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='Index'),
    path('products/', products, name='Products'),
]
