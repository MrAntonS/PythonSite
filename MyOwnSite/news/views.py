import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import News


def index(request, some_id=None):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Список новостей",
    }
    print(some_id)
    return render(request, 'news/index.html', context)


def test(request):
    return HttpResponse("<h1>Тестовая страница</h1>")
