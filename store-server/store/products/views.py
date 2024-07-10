from django.shortcuts import render


#функции = контроллеры = вьюхи

def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')