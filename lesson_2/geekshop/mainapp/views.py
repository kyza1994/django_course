from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html', )


links_menu = [
        {'href': 'products', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]


def contact(request):
    return render(request, 'mainapp/contact.html')


def products(request):
    content = {
        #'title': title,
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_home(request):
    content = {
        #'title': title,
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_office(request):
    content = {
        #'title': title,
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)

def products_modern(request):
    content = {
        #'title': title,
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_classic(request):
    content = {
        #'title': title,
        'links_menu': links_menu,
        #'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)