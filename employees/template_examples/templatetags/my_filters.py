from django import template

register = template.Library()


@register.filter(name='trunc5')
def trunc5(value):
    try:
        return value[:5]
    except (ValueError, TypeError) as e:
        return e
    # finally:
    #     return value
