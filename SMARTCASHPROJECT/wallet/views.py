from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from wallet import movements as mov

def home(request):
    return render(request, 'registration/home.html')

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():   
            form.save() 
            username = form.cleaned_data['username']
            #messages.success(request, f"Te has registrado correctamente{username}")        
            return redirect('dataaform')
    else: 
        form = UserRegisterForm()
        
    context = { 'form' : form }     
    return render(request, 'registration/register.html', context)


def login(request):
    
    return render(request,'registration/login.html') #redirigir al login

def data_form(request):
    average_income = request.GET.get('average_income')
    life_cost_average = request.GET.get('life_cost_average')
    month_income = request.GET.get('month_income')
    month_life_expenses = request.GET.get('month_life_expenses')
    month_expenses = request.GET.get('month_expenses')
    current_savings = request.GET.get('current_savings')
    print(average_income, life_cost_average, month_income, month_life_expenses, month_expenses, current_savings)
    return render(request, 'registration/data_form.html', {'average_income': average_income, 'life_cost_average': life_cost_average,
                                              'month_income': month_income, 'month_life_expenses': month_life_expenses,
                                              'month_expenses': month_expenses, 'current_savings': current_savings})
    
def movements(request):
    average_income = request.GET.get('average_income')
    life_cost_average = request.GET.get('life_cost_average')
    month_income = request.GET.get('month_income')
    month_life_expenses = request.GET.get('month_life_expenses')
    month_expenses = request.GET.get('month_expenses')
    current_savings = request.GET.get('current_savings')

    incomes = request.GET.get('incomes')
    exits = request.GET.get('exits')
    movements = mov.readIncomes(incomes) + mov.readExits(exits)
    print(incomes, exits)
    return render(request, 'registration/movements.html', {'average_income': average_income, 'life_cost_average': life_cost_average,
                                              'month_income': month_income, 'month_life_expenses': month_life_expenses,
                                              'month_expenses': month_expenses, 'current_savings': current_savings,
                                              'movements': movements})
                  
                  
        