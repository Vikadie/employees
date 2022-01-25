"""employees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from employees.employees_app.views import home, department_details, list_departments

# Mandatory, tuple or list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    # path('department/2/', department_details),
    # path('department/', list_departments),

    path('department/', include('employees.employees_app.urls')),
]
