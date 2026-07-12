from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import StoreConfig, Testimonial, Banner, InstagramReel, Location


@admin.register(StoreConfig)
class StoreConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('store_name', 'tagline', 'about_text', 'logo'),
        }),
        ('Contact', {
            'fields': ('whatsapp_number', 'instagram_url', 'facebook_url', 'email'),
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image'),
        }),
        ('Announcement & SEO', {
            'fields': ('announcement_text', 'meta_title', 'meta_description'),
        }),
    )

    def has_add_permission(self, request):
        return not StoreConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = StoreConfig.load()
        return HttpResponseRedirect(
            reverse('admin:store_config_storeconfig_change', args=[obj.pk])
        )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating', 'is_active', 'ordering')
    list_editable = ('is_active', 'ordering')
    list_filter = ('is_active', 'rating')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'is_active', 'ordering', 'starts_at', 'ends_at')
    list_editable = ('is_active', 'ordering')
    list_filter = ('position', 'is_active')


@admin.register(InstagramReel)
class InstagramReelAdmin(admin.ModelAdmin):
    list_display = ('title', 'reel_url', 'is_active', 'ordering')
    list_editable = ('is_active', 'ordering')
    list_filter = ('is_active',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'areas', 'phone', 'is_active', 'ordering')
    list_editable = ('is_active', 'ordering')
    list_filter = ('is_active',)
