from django.urls import URLPattern, path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('<int:some_id>', index, name='home'),
]