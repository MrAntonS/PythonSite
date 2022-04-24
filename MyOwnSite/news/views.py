from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import News, Category
from .forms import NewsForms


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


def add_new(request):
    if request.method == 'POST':
        form = NewsForms(request.POST)
        if form.is_valid():
            #form.cleaned_data
            News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = NewsForms()
    return render(request, 'news/add_news.html', {'form': form})
