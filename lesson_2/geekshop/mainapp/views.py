from django.shortcuts import render

def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


links_menu = [
        {'href': 'products', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_home(request):
    content = {
        'title': 'Продукты для дома',
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_office(request):
    content = {
        'title': 'Продукты для офиса',
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)

def products_modern(request):
    content = {
        'title': 'Продукты модерн',
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_classic(request):
    content = {
        'title': 'Продукты классика',
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)