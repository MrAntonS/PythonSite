from django.urls import URLPattern, path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('<int:some_id>', index, name='home'),
    path('add_new', add_new, name="add_news"),
]