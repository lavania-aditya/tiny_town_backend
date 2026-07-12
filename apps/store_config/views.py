from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import StoreConfig, Testimonial, Banner, InstagramReel, Location
from .serializers import (
    StoreConfigSerializer, TestimonialSerializer, BannerSerializer,
    InstagramReelSerializer, LocationSerializer,
)


class StoreConfigView(RetrieveAPIView):
    serializer_class = StoreConfigSerializer

    def get_object(self):
        return StoreConfig.load()


class TestimonialListView(ListAPIView):
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.filter(is_active=True)
    pagination_class = None


class BannerListView(ListAPIView):
    serializer_class = BannerSerializer
    pagination_class = None

    def get_queryset(self):
        from django.utils import timezone
        now = timezone.now()
        qs = Banner.objects.filter(is_active=True)
        qs = qs.exclude(starts_at__gt=now).exclude(ends_at__lt=now)
        position = self.request.query_params.get('position')
        if position:
            qs = qs.filter(position=position)
        return qs


class InstagramReelListView(ListAPIView):
    serializer_class = InstagramReelSerializer
    queryset = InstagramReel.objects.filter(is_active=True)
    pagination_class = None


class LocationListView(ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.filter(is_active=True)
    pagination_class = None
