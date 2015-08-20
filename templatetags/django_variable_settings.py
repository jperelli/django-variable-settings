from django import template
from .. import get

register = template.Library()


@register.simple_tag
def get_setting(name):
    try:
        return get(name)
    except:
        return ''
