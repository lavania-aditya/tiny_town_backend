from django.db.models import Count
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Category
from .serializers import CategoryListSerializer, CategoryDetailSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        qs = Category.objects.filter(is_active=True).annotate(
            children_count=Count('children', distinct=True),
            products_count=Count('products', distinct=True),
        )
        if self.request.query_params.get('top_level') == 'true':
            qs = qs.filter(parent__isnull=True)
        return qs

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategoryListSerializer
