from django.core.management.base import BaseCommand
from apps.categories.models import Category


CATEGORIES = [
    ('Learning & Educational', 'Puzzles, STEM kits, flash cards, and brain-building toys'),
    ('Fun Toys', 'Action figures, dolls, plushies, and playful favourites'),
    ('Miniature Vehicles', 'Die-cast cars, trucks, construction sets, and racing toys'),
    ('Board Games', 'Family board games, card games, and strategy games'),
    ('Pretend Play', 'Kitchen sets, doctor kits, tool benches, and dress-up'),
    ('Toddler Toys', 'Stacking rings, soft blocks, rattles, and sensory toys'),
    ('Keychains', 'Cute character keychains, novelty keychains, and collectibles'),
    ('Water Bottles', 'Fun printed water bottles and sippers for kids'),
    ('Novelty Items', 'Quirky gadgets, fidget toys, and unique gift items'),
    ('Return Gifts', 'Budget-friendly party favours and return gift packs'),
]


class Command(BaseCommand):
    help = 'Seed initial product categories'

    def handle(self, *args, **options):
        created = 0
        for i, (name, description) in enumerate(CATEGORIES):
            _, was_created = Category.objects.get_or_create(
                name=name,
                defaults={'description': description, 'ordering': i},
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f'Seeded {created} categories ({len(CATEGORIES)} total)'))
