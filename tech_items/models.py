from django.db import models

# Create your models here.
class Figure(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название фигуры')
    shape = models.CharField(max_length=50, verbose_name='Форма фигуры')
    text_color = models.CharField(max_length=20, verbose_name='Цвет текста')
    back_color = models.CharField(max_length=20, verbose_name='Цвет фона')
    border_color = models.CharField(max_length=20, verbose_name='Цвет границы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class ItemType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название типа элемента')
    figure = models.ForeignKey(Figure,
                               on_delete=models.PROTECT,
                               verbose_name='Фигура',
                               related_name='item_types')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип элемента'
        verbose_name_plural = 'Типы элементов'


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название элемента')
    type = models.ForeignKey(ItemType,
                             on_delete=models.PROTECT,
                             verbose_name='Тип элемента',
                             related_name='items')
    description = models.TextField(verbose_name='Описание элемента')
    icon = models.CharField(max_length=10, verbose_name='Иконка', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'


class LineEnd(models.Model):
    name = models.CharField(max_length=1, verbose_name='Название типа конца линии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип конца линии'
        verbose_name_plural = 'Типы концов линии'


class RelationType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название типа связи')
    icon = models.CharField(max_length=10, verbose_name='Иконка', blank=True)
    out_type = models.ForeignKey(ItemType,
                             on_delete=models.PROTECT,
                             verbose_name='Тип источника',
                             related_name='relation_out_types')
    out_type_mult = models.BooleanField(verbose_name='Группировка источников')
    in_type = models.ForeignKey(ItemType,
                             on_delete=models.PROTECT,
                             verbose_name='Тип приемника',
                             related_name='relation_in_types')
    in_type_mult = models.BooleanField(verbose_name='Группировка приемников')
    line_solid = models.BooleanField(verbose_name='Непрерывная')
    line_out_type = models.ForeignKey(LineEnd,
                                      on_delete=models.PROTECT,
                                      verbose_name='Конец источника',
                                      related_name='relation_type_out_set')
    line_in_type = models.ForeignKey(LineEnd,
                                     on_delete=models.PROTECT,
                                     verbose_name='Конец приемника',
                                     related_name='relation_type_in_set')
    line_color = models.CharField(max_length=20, verbose_name='Цвет линии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип взаимосвязи'
        verbose_name_plural = 'Типы взаимосвязей'


class Relation(models.Model):
    relation_type = models.ForeignKey(RelationType,
                                      on_delete=models.PROTECT,
                                      verbose_name='Тип взаимосвязи',
                                      related_name='relations')
    out_item = models.ForeignKey(Item,
                                 on_delete=models.PROTECT,
                                 verbose_name='Источник',
                                 related_name='relations_out')
    out_group_id = models.IntegerField(verbose_name='ID группы источника',
                                       null=True,
                                       blank=True,
                                       )
    out_group_sort = models.IntegerField(verbose_name='Индекс в группе источника',
                                         null=True,
                                         blank=True,
                                         )
    in_item = models.ForeignKey(Item,
                                 on_delete=models.PROTECT,
                                 verbose_name='Приемник',
                                 related_name='relations_in')
    in_group_id = models.IntegerField(verbose_name='ID группы приемника',
                                      null=True,
                                      blank=True,
                                      )
    in_group_sort = models.IntegerField(verbose_name='Индекс в группе приемника',
                                        null=True,
                                        blank=True,
                                        )

    def __str__(self):
        return f"{self.relation_type}: {self.out_item.name} - {self.in_item.name}"

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'
