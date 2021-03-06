from django import template

from django.utils.translation import ugettext

from .. import models

register = template.Library()

@register.filter
def variant_attrs(variant):
    if isinstance(variant, models.HatVariant) or not hasattr(variant, 'size') or not hasattr(variant, 'color'):
        return ()
    return ({'name': ugettext('Size'), 'value': variant.get_size_display()},
            {'name': ugettext('Color'), 'value': variant.get_color_display()})
