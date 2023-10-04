from django import template
from django.urls import reverse

from menu.models import MenuItem

register = template.Library()


def build_menu(menu_items, current_path):
    """
    Функция build_menu создает HTML-представление древовидного меню на основе списка menu_items и текущего URL current_path.

    :param menu_items: Список объектов MenuItem, представляющих пункты меню.
    :param current_path: Текущий URL, используется для определения активного пункта меню.
    :return: HTML-код для отображения меню.
    """
    menu_html = '<ul>'

    for item in menu_items:
        is_active = False
        if item.url_name:
            url = reverse(item.url_name)
            is_active = current_path.startswith(url)
        else:
            url = item.url

        menu_html += f'<li class={"active" if is_active else ""}><a href="{url}">{item.name}</a>'

        submenu_items = item.children.all()
        if submenu_items:
            menu_html += build_menu(submenu_items, current_path)

        menu_html += '</li>'

    menu_html += '</ul>'
    return menu_html


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Шаблонный тег draw_menu отрисовывает меню по его имени (menu_name) с учетом текущего URL из контекста (context).

    :param context: Контекст шаблона Django, содержащий информацию о текущем запросе.
    :param menu_name: Имя меню, которое используется для идентификации нужного меню.
    :return: HTML-код для отображения меню.
    """
    current_path = context['request'].path
    menu_items = MenuItem.objects.filter(parent__isnull=True, menu_name=menu_name).prefetch_related('children')

    if not menu_items:
        return ""

    return build_menu(menu_items, current_path)
