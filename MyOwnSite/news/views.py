from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import News, Category
from .forms import NewsForms


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Список новостей",
    }
    return render(request, 'news/index.html', context)


def test(request):
    return HttpResponse("<h1>Тестовая страница</h1>")


def add_new(request):
    if request.method == 'POST':
        form = NewsForms(request.POST)
        if form.is_valid():
            #form.cleaned_data
            news = form.save()
            return redirect(news)
    else:
        form = NewsForms()
    return render(request, 'news/add_news.html', {'form': form})

def get_one_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/show_one_news.html', {"title":"New", "news":news})
