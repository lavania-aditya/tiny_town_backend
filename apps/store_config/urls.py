from django.urls import path
from . import views

urlpatterns = [
    path('config/', views.StoreConfigView.as_view(), name='store-config'),
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial-list'),
    path('banners/', views.BannerListView.as_view(), name='banner-list'),
    path('reels/', views.InstagramReelListView.as_view(), name='reel-list'),
    path('locations/', views.LocationListView.as_view(), name='location-list'),
]
