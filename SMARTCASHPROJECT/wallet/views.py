from django.shortcuts import render
from django.http import HttpResponse


def data_form(request):
    average_income = request.GET.get('average_income')
    life_cost_average = request.GET.get('life_cost_average')
    month_income = request.GET.get('month_income')
    month_life_expenses = request.GET.get('month_life_expenses')
    month_expenses = request.GET.get('month_expenses')
    current_savings = request.GET.get('current_savings')
    print(average_income, life_cost_average, month_income, month_life_expenses, month_expenses, current_savings)
    return render(request, 'data_form.html', {'average_income': average_income, 'life_cost_average': life_cost_average,
                                              'month_income': month_income, 'month_life_expenses': month_life_expenses,
                                              'month_expenses': month_expenses, 'current_savings': current_savings})


def about(request):
    return HttpResponse('<h1>Welcome to About Page!!! </h1>')


def home(request):
    return render(request, 'home.html')

