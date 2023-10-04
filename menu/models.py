from django.db import models


class MenuItem(models.Model):
    """
    Модель MenuItem представляет пункты меню, которые можно использовать для создания древовидных меню.
    """
    name = models.CharField(
        max_length=100,
        help_text='Название пункта меню.'
    )
    url_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Имя URL-адреса для пункта меню (необязательно).'
    )
    url = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='URL-адрес для пункта меню (необязательно).'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        help_text='Родительский пункт меню, если он есть (необязательно).'
    )
    menu_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Название меню, к которому относится пункт меню (необязательно).'
    )

    class Meta:
        verbose_name = 'MenuItem'
        verbose_name_plural = 'MenuItems'

    def __str__(self):
        return self.name
