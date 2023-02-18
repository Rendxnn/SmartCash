from django.shortcuts import render
from django.http import HttpResponse


def data_form(request):
    return render(request, 'data_form.html')


def about(request):
    return HttpResponse('<h1>Welcome to About Page!!! </h1>')



