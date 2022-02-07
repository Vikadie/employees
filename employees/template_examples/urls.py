from django.urls import path

from employees.template_examples.views import template_examples

urlpatterns = [
    path('', template_examples, name='template examples')
]
