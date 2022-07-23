from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def HomePage(request):
    return HttpResponse('Hello')