from django.contrib import admin
from django import forms


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


class RelationAdmin(admin.ModelAdmin):
    form = RelationAdminForm


admin.site.register(Relation, RelationAdmin)

# admin.site.register(Relation)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(RelationType)
admin.site.register(Figure)
admin.site.register(LineEnd)
