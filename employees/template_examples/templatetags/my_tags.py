from django import template

from employees.employees_app.models import Department

register = template.Library()


@register.simple_tag
# def get_verbose_name(obj, fieldnm):
#   return obj._meta.get_field(fieldnm).verbose_name
def get_verbose_name(obj):
    return obj._meta.verbose_name  # not working as expected


@register.inclusion_tag('tags/department_tag.html')
def get_departments():
    departments_list = Department.objects.prefetch_related('employee_set').all()
    return {
        'departments': departments_list,
    }
