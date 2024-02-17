from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'name': "Login App"
    }
    return render(request, 'index.html', context)
