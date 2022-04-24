from django.urls import URLPattern, path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('add_new', add_new, name="add_news"),
    path('<int:news_id>', get_one_news, name="get_one_news"),
]