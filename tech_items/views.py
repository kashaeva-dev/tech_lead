from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Item, RelationType

def index(request):
    return render(request, 'tech_items/index.html',
                  )


class FilterOutItemView(View):
    def get(self, request):
        relation_type_id = request.GET.get('relation_type')
        data = []
        if relation_type_id:
            try:
                relation_type = RelationType.objects.get(pk=relation_type_id)
                items = Item.objects.filter(type=relation_type.out_type)
                data = [{'id': item.id, 'name': item.name} for item in items]
            except RelationType.DoesNotExist:
                pass
        return JsonResponse({'items': data})


class FilterInItemView(View):
    def get(self, request):
        relation_type_id = request.GET.get('relation_type')
        data = []
        if relation_type_id:
            try:
                relation_type = RelationType.objects.get(pk=relation_type_id)
                # Assuming 'in_item_type' is the field that references ItemType for in items
                items = Item.objects.filter(type=relation_type.in_type)
                data = [{'id': item.id, 'name': item.name} for item in items]
            except RelationType.DoesNotExist:
                pass
        return JsonResponse({'items': data})