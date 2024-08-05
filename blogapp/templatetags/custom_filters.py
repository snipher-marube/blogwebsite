from django import template

register = template.Library()

@register.filter(name='titlecase')
def titlecase(value):
    return value.title()