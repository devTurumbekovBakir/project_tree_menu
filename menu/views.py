from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def nested_menu(request):
    return render(request, 'nested_menu.html')


def product_detail(request, product_id):
    return render(request, 'product_detail.html')


def multi_menu(request):
    return render(request, 'multi_menu.html')


def dynamic_url_menu(request, category_id):
    return render(request, 'dynamic_url_menu.html')
