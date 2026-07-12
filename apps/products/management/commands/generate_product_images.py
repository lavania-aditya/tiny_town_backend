import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont
from apps.products.models import Product, ProductImage


CATEGORY_COLORS = {
    'vehicles-rc': ('#FF4D4F', '#FF8A8C'),
    'puzzles-games': ('#409EFF', '#79BFFF'),
    'art-stationery': ('#FFD23F', '#FFE27A'),
    'soft-toys-keychains': ('#4CAF50', '#81C784'),
    'pretend-play': ('#9C27B0', '#CE93D8'),
    'everyday-gifting': ('#FF9800', '#FFB74D'),
}

CATEGORY_EMOJIS = {
    'vehicles-rc': '🚗',
    'puzzles-games': '🧩',
    'art-stationery': '🎨',
    'soft-toys-keychains': '🧸',
    'pretend-play': '👨‍🍳',
    'everyday-gifting': '🎁',
}


def create_product_image(product_name, category_slug, size=(800, 800)):
    colors = CATEGORY_COLORS.get(category_slug, ('#6366F1', '#A5B4FC'))
    bg_color = colors[0]
    accent = colors[1]

    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)

    center_x, center_y = size[0] // 2, size[1] // 2

    draw.rounded_rectangle(
        [center_x - 200, center_y - 200, center_x + 200, center_y + 200],
        radius=30,
        fill=accent,
    )

    draw.rounded_rectangle(
        [center_x - 160, center_y - 160, center_x + 160, center_y + 160],
        radius=20,
        fill='white',
        outline=bg_color,
        width=3,
    )

    try:
        font_large = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
        font_small = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
    except (OSError, IOError):
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    words = product_name.split()
    lines = []
    current_line = ''
    for word in words:
        test_line = f'{current_line} {word}'.strip()
        if len(test_line) > 18:
            if current_line:
                lines.append(current_line)
            current_line = word
        else:
            current_line = test_line
    if current_line:
        lines.append(current_line)

    text_y = center_y - (len(lines) * 18)
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font_large)
        text_w = bbox[2] - bbox[0]
        draw.text((center_x - text_w // 2, text_y), line, fill=bg_color, font=font_large)
        text_y += 36

    label = f'Tiny Town Creations'
    bbox = draw.textbbox((0, 0), label, font=font_small)
    label_w = bbox[2] - bbox[0]
    draw.text(
        (center_x - label_w // 2, size[1] - 60),
        label,
        fill='white',
        font=font_small,
    )

    for i in range(4):
        x = 60 + i * 40
        draw.ellipse([x, 50, x + 20, 70], fill=accent)
    for i in range(4):
        x = size[0] - 60 - i * 40
        draw.ellipse([x - 20, size[1] - 70, x, size[1] - 50], fill=accent)

    return img


class Command(BaseCommand):
    help = 'Generate placeholder product images for all products without images'

    def handle(self, *args, **options):
        products = Product.objects.filter(is_active=True)
        created = 0

        os.makedirs('media/products', exist_ok=True)

        for product in products:
            if product.images.exists():
                self.stdout.write(f'  Skipping {product.name} (already has images)')
                continue

            img = create_product_image(product.name, product.category.slug)

            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85)
            buffer.seek(0)

            filename = f'{product.slug}.jpg'
            product_image = ProductImage(
                product=product,
                alt_text=product.name,
                is_primary=True,
                ordering=0,
            )
            product_image.image.save(filename, ContentFile(buffer.read()), save=True)
            created += 1
            self.stdout.write(f'  Created image for: {product.name}')

        self.stdout.write(self.style.SUCCESS(f'Generated {created} product images.'))
