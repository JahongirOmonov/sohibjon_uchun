from django import template

register = template.Library()

@register.filter
def split(value, key):
    """Splits the string by the given key (space, comma, etc.)."""
    return value.split(key)