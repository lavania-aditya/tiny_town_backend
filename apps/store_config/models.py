from django.db import models
from cloudinary.models import CloudinaryField


class StoreConfig(models.Model):
    store_name = models.CharField(max_length=200, default='Tiny Town Creations')
    tagline = models.CharField(max_length=300, blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    about_text = models.TextField(blank=True)
    logo = CloudinaryField('image', blank=True, null=True)
    hero_image = CloudinaryField('image', blank=True, null=True)
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.CharField(max_length=300, blank=True)
    announcement_text = models.CharField(
        max_length=500, blank=True,
        help_text='Text shown in the announcement bar at the top',
    )
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Store Configuration'
        verbose_name_plural = 'Store Configuration'

    def __str__(self):
        return self.store_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    avatar_color = models.CharField(
        max_length=20, default='#FF4D4F',
        help_text='Hex color for avatar circle',
    )
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return f'{self.name} — {self.location}'


class Banner(models.Model):
    POSITION_CHOICES = [
        ('hero', 'Hero Section'),
        ('announcement', 'Announcement Bar'),
        ('promo', 'Promotional Banner'),
    ]

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    link_url = models.URLField(blank=True)
    link_text = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='promo')
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class InstagramReel(models.Model):
    title = models.CharField(max_length=200, blank=True)
    reel_url = models.URLField(help_text='Instagram reel URL')
    thumbnail = CloudinaryField('image', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title or f'Reel {self.pk}'


class Location(models.Model):
    city = models.CharField(max_length=100)
    areas = models.CharField(max_length=300, blank=True, help_text='Comma-separated area names')
    phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    google_maps_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.city
