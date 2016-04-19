from django import template
from .. import get

register = template.Library()


@register.simple_tag
def get_setting(name, default=''):
    try:
        value = get(name)
        if value is not None:
            return value
        else:
            return default
    except:
        return default
