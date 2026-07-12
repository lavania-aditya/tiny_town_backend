import os
from django.db import models
from django.utils.text import slugify
from apps.categories.models import Category, Tag

_use_cloudinary = (
    os.environ.get('CLOUDINARY_CLOUD_NAME', '') not in ('', 'your-cloud-name')
)

if _use_cloudinary:
    from cloudinary.models import CloudinaryField


class Product(models.Model):
    AGE_CHOICES = [
        ('0-2', '0–2 years'),
        ('3-5', '3–5 years'),
        ('6-8', '6–8 years'),
        ('9-12', '9–12 years'),
        ('13+', '13+ years'),
        ('all', 'All ages'),
    ]

    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=320, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_at_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text='Original MRP for showing discount',
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products',
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    age_range = models.CharField(max_length=5, choices=AGE_CHOICES, default='all')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def discount_percentage(self):
        if self.compare_at_price and self.compare_at_price > self.price:
            return round((1 - self.price / self.compare_at_price) * 100)
        return 0

    @property
    def primary_image(self):
        img = self.images.filter(is_primary=True).first()
        if not img:
            img = self.images.first()
        return img


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images',
    )
    image = CloudinaryField('image') if _use_cloudinary else models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return f'{self.product.name} — Image {self.ordering}'


class ProductVideo(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='videos',
    )
    video = CloudinaryField('video', resource_type='video') if _use_cloudinary else models.FileField(upload_to='products/videos/')
    title = models.CharField(max_length=200, blank=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return f'{self.product.name} — Video {self.ordering}'
