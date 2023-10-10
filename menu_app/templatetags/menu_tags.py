from django import template
from menu_app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    return {'menu_items': menu_items, 'request': request}
