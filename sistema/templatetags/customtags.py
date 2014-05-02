from django import template
import re

register = template.Library()

def safe_tags(value):
    """Returns the given HTML with all tags stripped."""
    return re.sub(r'<(?!/?(p|span|(h+[0-9])|style|div|br|hr))[^>]*?>', '', unicode(value))
safe_tags.is_safe = True
register.filter('safe_tags', safe_tags)