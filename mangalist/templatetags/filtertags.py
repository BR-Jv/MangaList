from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="status")
@stringfilter
def status(value):
    if value == 'l':
        return "Em lançamento"
    elif value == 'h':
        return "Em hiato" 
    elif value == 'f':
        return "Finalizado" 