from django import template

register = template.Library()

@register.simple_tag
def media(value):
    if value:
        return f'/media/{value}'
    return '#'

@register.filter()
def media(value):
    if value:
        return f'/media/{value}'
    return '#'

