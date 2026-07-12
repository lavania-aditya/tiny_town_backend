import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__slug')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    tag = django_filters.CharFilter(field_name='tags__slug')

    class Meta:
        model = Product
        fields = ['is_featured', 'age_range']
