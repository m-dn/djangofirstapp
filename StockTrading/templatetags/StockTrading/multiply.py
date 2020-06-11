from django import template

register = template.Library()

@register.simple_tag()
def multiply(price, quantity, *args, **kwargs):
    return price * quantity