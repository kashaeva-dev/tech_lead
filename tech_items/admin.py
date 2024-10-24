from django import forms
from django.contrib import admin
from django.forms import Select
from django.utils.html import format_html
from django.db import models

from tech_items.models import Relation, Item, RelationType, Figure, ItemType, LineEnd


class RelationAdminForm(forms.ModelForm):
    class Meta:
        model = Relation
        fields = '__all__'

    class Media:
        js = (
            'admin/js/vendor/jquery/jquery.js',  # Django's built-in jQuery
            'js/relation-admin.js',
        )

@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    form = RelationAdminForm
    list_display = [
        'relation_type',
        'out_item',
        'in_item',
        'out_group_id',
        'out_group_sort',
        'in_group_id',
        'in_group_sort',
    ]
    list_editable = [
        'out_group_id',
        'out_group_sort',
        'in_group_id',
        'in_group_sort',
    ]
    list_display_links = ('relation_type',)
    list_filter = ['relation_type', 'out_item', 'in_item']

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        form_field = super().formfield_for_dbfield(db_field, request, **kwargs)

        if db_field.name == 'out_group_id':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 30px;',
            })

        if db_field.name == 'out_group_sort':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 30px;',
            })

        if db_field.name == 'in_group_id':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 30px;',
            })

        if db_field.name == 'in_group_sort':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 30px;',
            })

        return form_field

@admin.register(RelationType)
class RelationTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'icon',
        'out_type',
        'out_type_mult',
        'in_type',
        'in_type_mult',
        'line_solid',
        'line_out_type',
        'line_in_type',
        'line_color',
        'line_color_preview',
    ]

    def line_color_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 30px; background-color: {};"></div>',
            obj.line_color
        )

    line_color_preview.short_description = 'Цвет'

    list_editable = [
        'icon',
        'out_type_mult',
        'in_type_mult',
        'line_solid',
        'line_out_type',
        'line_in_type',
        'line_color',
    ]
    list_display_links = ('name',)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        form_field = super().formfield_for_dbfield(db_field, request, **kwargs)

        if db_field.name == 'line_out_type':
            form_field.widget = forms.Select(attrs={
                'style': 'width: 40px;',
            })

        if db_field.name == 'line_in_type':
            form_field.widget = forms.Select(attrs={
                'style': 'width: 40px;',
            })

        if db_field.name == 'icon':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 20px;',
            })

        if db_field.name == 'line_color':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 60px;',
            })

        return form_field


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'figure',
    ]
    list_editable = [
        'figure',
    ]
    list_display_links = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'type',
        'description',
        'icon',
    ]
    list_editable = [
        'type',
        'description',
        'icon',
    ]
    list_display_links = ('name',)
    list_filter = ['type']

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        form_field = super().formfield_for_dbfield(db_field, request, **kwargs)

        if db_field.name == 'description':
            form_field.widget = forms.Textarea(attrs={
                'rows': 3,
                'cols': 50,
            })

        if db_field.name == 'icon':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 20px;',
            })

        if db_field.name == 'type':
            form_field.widget = forms.Select(attrs={
                'style': 'width: 100px;',
            })

        return form_field


@admin.register(LineEnd)
class LineEndAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    list_editable = [
    ]
    list_display_links = ('name',)


@admin.register(Figure)
class FigureAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'shape',
        'text_color',
        'text_color_preview',
        'back_color',
        'back_color_preview',
        'border_color',
        'border_color_preview',
    ]

    def text_color_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 30px; background-color: {};"></div>',
            obj.text_color
        )
    text_color_preview.short_description = 'Цвет'

    def back_color_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 30px; background-color: {};"></div>',
            obj.back_color
        )
    back_color_preview.short_description = 'Цвет'

    def border_color_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 30px; background-color: {};"></div>',
            obj.border_color
        )
    border_color_preview.short_description = 'Цвет'

    list_editable = [
        'shape',
        'text_color',
        'back_color',
        'border_color',
    ]
    list_display_links = ('name',)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        form_field = super().formfield_for_dbfield(db_field, request, **kwargs)

        if db_field.name == 'text_color':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 60px;',  # Уменьшаем ширину поля
            })

        if db_field.name == 'back_color':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 60px;',
            })

        if db_field.name == 'border_color':
            form_field.widget = forms.TextInput(attrs={
                'style': 'width: 60px;',
            })

        return form_field
