from rest_framework import serializers
from apps.categories.serializers import CategoryBriefSerializer, TagSerializer
from .models import Product, ProductImage, ProductVideo


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary', 'ordering']

    def get_image(self, obj):
        if not obj.image:
            return None
        url = obj.image.url if hasattr(obj.image, 'url') else str(obj.image)
        request = self.context.get('request')
        if request and url.startswith('/'):
            return request.build_absolute_uri(url)
        return url


class ProductVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = ['id', 'video', 'title', 'ordering']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryBriefSerializer(read_only=True)
    primary_image = serializers.SerializerMethodField()
    discount_percentage = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'price', 'compare_at_price',
            'category', 'primary_image', 'discount_percentage',
            'is_featured', 'age_range',
        ]

    def get_primary_image(self, obj):
        img = obj.primary_image
        if not img:
            return None
        request = self.context.get('request')
        url = img.image.url if hasattr(img.image, 'url') else str(img.image)
        if request and url.startswith('/'):
            return request.build_absolute_uri(url)
        return url


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryBriefSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    videos = ProductVideoSerializer(many=True, read_only=True)
    discount_percentage = serializers.IntegerField(read_only=True)
    related_products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'compare_at_price',
            'category', 'tags', 'images', 'videos', 'discount_percentage',
            'is_featured', 'age_range', 'created_at', 'related_products',
        ]

    def get_related_products(self, obj):
        related = Product.objects.filter(
            category=obj.category, is_active=True,
        ).exclude(pk=obj.pk)[:4]
        return ProductListSerializer(related, many=True).data
