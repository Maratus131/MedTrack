from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse
from django.template.loader import render_to_string

from trackmed.models import User

menu = [{'title': "О компании", 'url_name':'about'},
        {'title': "Программа", 'url_name':'program'},
        {'title': "Руководство",'url_name':'manual'}
]

def index(request):
    return render(request, 'trackmed/index.html', {'title': 'MedTrack', 'menu':menu})

def about(request):
    return render(request, 'trackmed/aboutCompany.html', {'title': 'MedTrack - О компании', 'menu': menu})

def manual(request):
    return render(request, 'trackmed/manual.html', {'title': 'MedTrack - Руководство', 'menu': menu})

def program(request):
    return render(request, 'trackmed/program.html', {'title': 'MedTrack - Программа', 'menu': menu})


def show_user(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'trackmed/user.html', {'user': user})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")