from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    content = {
        'title': 'главная',
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


def products(request, pk=None):
    content = {
        'title': 'Продукты',
        'links_menu': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', content)
