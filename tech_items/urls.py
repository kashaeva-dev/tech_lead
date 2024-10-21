from django.urls import path

from .views import index, FilterOutItemView, FilterInItemView

urlpatterns = [
    path('', index, name='index'),
    path('ajax/filter-out-item/', FilterOutItemView.as_view(), name='filter_out_item'),
    path('ajax/filter-in-item/', FilterInItemView.as_view(), name='filter_in_item'),
]