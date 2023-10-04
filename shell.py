from menu.models import MenuItem

# Простое горизонтальное меню
# Создание главного меню
main_menu1 = MenuItem.objects.create(name='Главная', menu_name='main_menu1')

# Пункты меню
MenuItem.objects.create(name='О нас', url='/about/', parent=main_menu1)
MenuItem.objects.create(name='Контакты', url='/contact/', parent=main_menu1)

# ----------------------------------------------------------------------------------------------------------------------

# Вложенные меню
# Создание вложенного меню
nested_menu = MenuItem.objects.create(name='Навигация', menu_name='nested_menu')

# Пункты меню
item1 = MenuItem.objects.create(name='Пункт 1', parent=nested_menu)
item2 = MenuItem.objects.create(name='Пункт 2', parent=nested_menu)
item3 = MenuItem.objects.create(name='Пункт 3', parent=nested_menu)

# Вложенные пункты меню
MenuItem.objects.create(name='Подпункт 1.1', parent=item1)
MenuItem.objects.create(name='Подпункт 1.2', parent=item1)
MenuItem.objects.create(name='Подпункт 2.1', parent=item2)

# ----------------------------------------------------------------------------------------------------------------------

# Активный пункт меню
# Создание главного меню
main_menu2 = MenuItem.objects.create(name='Main Menu 2', menu_name='main_menu2')

# Создать пункты меню для main_menu2
MenuItem.objects.create(name='О нас', url='/about/', parent=main_menu2)
MenuItem.objects.create(name='Контакты', url='/contact/', parent=main_menu2)
MenuItem.objects.create(name='Продукт 1', url='/product_detail/', parent=main_menu2)


# ----------------------------------------------------------------------------------------------------------------------

# Множество меню на одной странице
# Создание главного меню
main_menu3 = MenuItem.objects.create(name='Главное меню', menu_name='main_menu3')

# Пункты главного меню
MenuItem.objects.create(name='О нас', url='/about/', parent=main_menu3)
MenuItem.objects.create(name='Контакты', url='/contact/', parent=main_menu3)

# Создание второго меню
secondary_menu = MenuItem.objects.create(name='Второе меню', menu_name='secondary_menu')

# Пункты второго меню
MenuItem.objects.create(name='Пункт 1', url='/menu1/', parent=secondary_menu)
MenuItem.objects.create(name='Пункт 2', url='/menu2/', parent=secondary_menu)

# ----------------------------------------------------------------------------------------------------------------------

# Меню с динамическими URL
# Создание меню с динамическими URL
dynamic_menu = MenuItem.objects.create(name='Динамическое меню', menu_name='dynamic_menu')

# Пункты меню с динамическими URL
MenuItem.objects.create(name='Категория 1', url='/category/1/', parent=dynamic_menu)
MenuItem.objects.create(name='Категория 2', url='/category/2/', parent=dynamic_menu)
MenuItem.objects.create(name='Категория 3', url='/category/3/', parent=dynamic_menu)
