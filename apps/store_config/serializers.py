from rest_framework import serializers
from .models import StoreConfig, Testimonial, Banner, InstagramReel, Location


class StoreConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreConfig
        fields = [
            'store_name', 'tagline', 'whatsapp_number', 'instagram_url',
            'facebook_url', 'email', 'about_text', 'logo', 'hero_image',
            'hero_title', 'hero_subtitle', 'announcement_text',
            'meta_title', 'meta_description',
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'location', 'text', 'rating', 'avatar_color']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'title', 'subtitle', 'image', 'link_url', 'link_text', 'position']


class InstagramReelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramReel
        fields = ['id', 'title', 'reel_url', 'thumbnail']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'areas', 'phone', 'whatsapp_number', 'address', 'google_maps_url']
