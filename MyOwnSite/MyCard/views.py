from django.shortcuts import render

# Create your views here.


def index(request):
    print("Im doing this just to stay on track bruh")
    return render(request, 'MyCard/index.html')
