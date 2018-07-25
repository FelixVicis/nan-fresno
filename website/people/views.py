from django.shortcuts import render
from django.http import HttpResponse
from .models import People
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.


@login_required(login_url="/admin")
def index(request):
    # return HttpResponse('hello from people')

    people_list = People.objects.all()

    query = request.GET.get("q")
    if query:
        people_list = people_list.filter(
            Q(firstName__icontains=query) or
            Q(lastName__icontains=query) or
            Q(city__icontains=query) or
            Q(state__icontains=query) or
            Q(county__icontains=query) or
            Q(country__icontains=query) or
            Q(circumstance__icontains=query) or
            Q(age__icontains=query) or
            Q(sex__icontains=query) or
            Q(race__icontains=query) or
            Q(eye_color__icontains=query) or
            Q(hair_color__icontains=query)
        ).distinct()

    paginator = Paginator(people_list, 12)  # Show 12 persons per page

    page = request.GET.get('page')
    people = paginator.get_page(page)
    return render(request, 'people/people_list.html', {'people': people})

    context = {
        'title': 'Missing Persons',
        'people': people
    }
    return render(request, 'people/index.html', context)


# @login_required(login_url="/admin")
# def details(request, id):
#     person = People.objects.get(id=id)
#     context = {
#         'person': person
#     }
#     return render(request, 'people/details.html', context)

def details(request, id):
    person = People.objects.get(id=id)
    context = {
        'person': person
    }
    return render(request, 'people/details.html', context)
