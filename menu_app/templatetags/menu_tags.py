from django import template
from menu_app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    active_item = MenuItem.objects.filter(menu_name=menu_name, url=request.path).first()
    print(active_item, menu_name, request.path)
    if active_item:
        parents = list(active_item.get_ancestors()) + [active_item,]
        parent_ids = [parent.id for parent in parents] + [active_item.id,] 
        children = list(active_item.get_children()) 
    else:
        base = MenuItem.objects.filter(menu_name=menu_name, url='/').first()
        parents = [base, ]
        parent_ids = [base.pk, ]
        children = []
    return {'active_item': active_item, 'parents': parents, 'parent_ids': parent_ids, 'children': children, 'request': request}

