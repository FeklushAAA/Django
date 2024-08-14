
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import index, products

#Набор уникальных путей к именам файлов для перехода на отдельные страницы
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', products, name='products'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)