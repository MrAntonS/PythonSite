from django.urls import re_path, path
from .views import *


urlpatterns = [
    path('', HomePage, name='PWA home page')
]