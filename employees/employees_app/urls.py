from django.urls import path

from employees.employees_app.views import department_details, list_departments

urlpatterns = [
    path('<int:id>/', department_details, name='department details'),
    path('', list_departments, name='departments list'),
]
