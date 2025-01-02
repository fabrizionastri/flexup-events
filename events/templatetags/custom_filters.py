from django import template

register = template.Library()


@register.filter
def get_item(obj, attr):
    return getattr(obj, attr)
