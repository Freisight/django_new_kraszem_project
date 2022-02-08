from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from .models import *

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'Контакты', 'url_name': 'about'}
]

def index(request):
    cottages = Cottage.objects.all()
    context = {'cottages': cottages, 'menu': menu, 'title': 'Главная страница'}
    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about.html',  {'menu': menu, 'title': 'О компании'})

def direct(request):
    pass

def village(request, cottage_id, direct):
    cottage_info = Cottage.objects.get(pk=cottage_id)
    context = {'menu': menu, 'info': cottage_info}
    return render(request, 'main/cottage.html', context=context)

# def news(request):
#     if(request.GET):
#         print(request.GET)
#     # Сделалано условем, если есть, то выведем, чтьобы не было ошибки.
#     # просто для теста запихал сюда показ гет запросы с url
#     return render(request, 'main/news.html')

# def newsCat(request, cat):
#     return render(request, 'main/news.html')


# НА случай если мы выдает ошибку 404 при ненужных страницах.
# def archive(request, year):
#     if int(year) > 2022:
#         raise Http404()
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year} год</p>')

# Редирект вместо несуществующей страницы.
# def archive(request, year):
#     if int(year) > 2022:
#         return redirect('home', permanent=True)
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year} год</p>')


def pageNotFound(request, exception):
    return render(request, 'main/404.html')
