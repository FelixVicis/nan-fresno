from django.shortcuts import render


# Create your views here.


def index(request):

    context = {
        'title': 'Missing Persons',
    }
    return render(request, 'marketing/index.html', context)
