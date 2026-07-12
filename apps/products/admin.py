from django.contrib import admin
from .models import Product, ProductImage, ProductVideo


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active', 'is_featured', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['is_active', 'is_featured', 'category', 'age_range']
    search_fields = ['name', 'description']
    filter_horizontal = ['tags']
    inlines = [ProductImageInline, ProductVideoInline]
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'description')}),
        ('Pricing', {'fields': ('price', 'compare_at_price')}),
        ('Classification', {'fields': ('category', 'tags', 'age_range')}),
        ('Visibility', {'fields': ('is_active', 'is_featured')}),
    )
