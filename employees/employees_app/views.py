from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from employees.employees_app.models import Department, Employee


def home(request):
    context = {
        'number': 23,
    }
    return render(request, 'base/base.html', context)


def department_details(request, id):
    return HttpResponse(f'This is department {id}')


def list_departments(request):
    context = {
        'departments': Department.objects.prefetch_related('employee_set').all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)
