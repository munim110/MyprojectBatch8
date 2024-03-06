from django.shortcuts import render

# Create your views here.


def hello(request):
    context = {
        'name': 'Najmul Hossain Shanto',
        'age': 35
    }
    return render(request, 'hello.html', context)


def hi(request):
    return render(request, 'page.html')