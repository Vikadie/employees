from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from employees.employees_app.models import Employee


def template_examples(response):
    context = {
        'title': 'Template Examples',
        'employees': Employee.objects.order_by('-company', '-last_name', '-first_name').all(),
    }
    return render(response, 'template_examples/index.html', context)
