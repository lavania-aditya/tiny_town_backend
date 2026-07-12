from django.core.management.base import BaseCommand
from apps.store_config.models import Testimonial, Location, InstagramReel
from apps.categories.models import Category
from apps.products.models import Product


class Command(BaseCommand):
    help = 'Seed testimonials, locations, and sample products from the existing tinytowncreations.in site'

    def handle(self, *args, **options):
        self._seed_testimonials()
        self._seed_locations()
        self._seed_reels()
        self._seed_products()
        self.stdout.write(self.style.SUCCESS('Seeding complete.'))

    def _seed_testimonials(self):
        testimonials = [
            {
                'name': 'Priya S.',
                'location': 'Indirapuram',
                'text': 'Ordered a birthday hamper and the kids went absolutely crazy! The packaging was so beautiful. Will definitely order again.',
                'avatar_color': '#FF4D4F',
            },
            {
                'name': 'Anjali M.',
                'location': 'Vaishali',
                'text': "Return gifts for my son's birthday party were a huge hit! All 30 kids loved them. Quality was amazing and delivery was superfast.",
                'avatar_color': '#409EFF',
            },
            {
                'name': 'Renu K.',
                'location': 'Indirapuram',
                'text': "The keychains and fidget toys are SO cute! My daughter couldn't put them down. WhatsApp support was super helpful.",
                'avatar_color': '#4CAF50',
            },
            {
                'name': 'Sneha T.',
                'location': 'Vasundhara',
                'text': 'Ordered 50 return gift sets for a school function. Flawless packaging, quick delivery — the kids loved them.',
                'avatar_color': '#9C27B0',
            },
            {
                'name': 'Vikram D.',
                'location': 'Indirapuram',
                'text': 'The puzzle set kept my twins busy for hours! Great for screen-free time, beautiful finish, came in a lovely gift box.',
                'avatar_color': '#FF9800',
            },
            {
                'name': 'Nisha B.',
                'location': 'Vaishali',
                'text': 'Perfect gifts for my niece — she loved the plush toys! The WhatsApp ordering was smooth and the team was very helpful.',
                'avatar_color': '#FFD23F',
            },
        ]

        if Testimonial.objects.exists():
            self.stdout.write('Testimonials already seeded, skipping.')
            return

        for i, t in enumerate(testimonials):
            Testimonial.objects.create(ordering=i, **t)
        self.stdout.write(f'Created {len(testimonials)} testimonials.')

    def _seed_locations(self):
        locations = [
            {
                'city': 'Ghaziabad',
                'areas': 'Indirapuram, Vaishali, Vasundhara',
                'phone': '9891943797',
                'whatsapp_number': '919891943797',
            },
            {
                'city': 'Delhi',
                'areas': 'Vasundhara Enclave, Mayur Vihar',
                'phone': '9315400375',
                'whatsapp_number': '919315400375',
            },
            {
                'city': 'Gurgaon',
                'areas': 'Sector 9',
                'phone': '9717772465',
                'whatsapp_number': '919717772465',
            },
        ]

        if Location.objects.exists():
            self.stdout.write('Locations already seeded, skipping.')
            return

        for i, loc in enumerate(locations):
            Location.objects.create(ordering=i, **loc)
        self.stdout.write(f'Created {len(locations)} locations.')

    def _seed_reels(self):
        reel_ids = [
            'DHt1hH2Tfi9', 'DHqFUFRz6M5', 'DHm_bw-TkXi', 'DHX0vSHzFvh',
            'DHUxqU0TnO5', 'DHSV3HVTnVU', 'DHMz-YLzLlI', 'DHKo6lgTlXP',
            'DHHcN76zpuP', 'DHFG5NMTRxi', 'DHCwciqzsgO', 'DG_d_9jz40c',
            'DG8mkUcT_7R', 'DG50iG7TMQF', 'DG3qokHTLsI', 'DG1VzpfTDK3',
            'DGyKE2lztpZ', 'DGv3KHdzBSC', 'DGt8UjFzNsL', 'DGp6hWpTLGR',
            'DGnZ8njzPRK', 'DGlDg3CTefy', 'DGh63oVzQKs', 'DGfvCYeTEZJ',
            'DGdTvZ5z4ks', 'DGbP8L1TYzU', 'DGZB3tZz8kG', 'DGW3Ge_zeqe',
        ]

        if InstagramReel.objects.exists():
            self.stdout.write('Reels already seeded, skipping.')
            return

        for i, reel_id in enumerate(reel_ids):
            InstagramReel.objects.create(
                title=f'Reel {i + 1}',
                reel_url=f'https://www.instagram.com/reel/{reel_id}/',
                ordering=i,
            )
        self.stdout.write(f'Created {len(reel_ids)} Instagram reels.')

    def _seed_products(self):
        if Product.objects.exists():
            self.stdout.write('Products already exist, skipping.')
            return

        category_map = {}
        for cat in Category.objects.all():
            category_map[cat.slug] = cat

        products = [
            {'name': 'Mini RC Drift Car', 'price': 599, 'compare_at_price': 999, 'category': 'vehicles-rc', 'description': 'Multifunctional mini drift car with remote control, perfect for kids who love racing.', 'is_featured': True},
            {'name': 'Monster Truck RC', 'price': 899, 'compare_at_price': 1499, 'category': 'vehicles-rc', 'description': 'High-speed monster truck with big wheels, handles rough terrain.', 'is_featured': True},
            {'name': 'Die-Cast Car Set (6 Pcs)', 'price': 399, 'compare_at_price': 699, 'category': 'vehicles-rc', 'description': 'Set of 6 premium die-cast metal cars in a gift box.'},
            {'name': '3D Wooden Puzzle - Dinosaur', 'price': 349, 'compare_at_price': 599, 'category': 'puzzles-games', 'description': '3D wooden puzzle dinosaur kit, great for building skills.', 'is_featured': True},
            {'name': 'Rubik\'s Cube 3x3', 'price': 199, 'compare_at_price': 349, 'category': 'puzzles-games', 'description': 'Classic 3x3 Rubik\'s Cube, smooth turning and durable.'},
            {'name': 'Chess & Ludo 2-in-1 Board', 'price': 449, 'compare_at_price': 799, 'category': 'puzzles-games', 'description': 'Premium wooden chess and ludo combo board game.'},
            {'name': 'Art & Craft Kit Deluxe', 'price': 699, 'compare_at_price': 1199, 'category': 'art-stationery', 'description': '150-piece art supplies kit with crayons, markers, paints and more.', 'is_featured': True},
            {'name': 'Magic Scratch Art Cards (10 Pcs)', 'price': 249, 'compare_at_price': 449, 'category': 'art-stationery', 'description': 'Rainbow scratch art cards with stylus, great for creative fun.'},
            {'name': 'Stationery Gift Set', 'price': 299, 'compare_at_price': 499, 'category': 'art-stationery', 'description': 'Cute stationery set with pencils, erasers, ruler and pencil case.'},
            {'name': 'Plush Teddy Bear (12 inch)', 'price': 499, 'compare_at_price': 899, 'category': 'soft-toys-keychains', 'description': 'Super soft teddy bear, perfect for cuddling. Makes a great gift.', 'is_featured': True},
            {'name': 'Keychain Set - Cartoon Characters (5 Pcs)', 'price': 199, 'compare_at_price': 349, 'category': 'soft-toys-keychains', 'description': 'Set of 5 cute cartoon character keychains.'},
            {'name': 'Fidget Pop-It Keychain', 'price': 99, 'compare_at_price': 199, 'category': 'soft-toys-keychains', 'description': 'Mini pop-it fidget toy keychain, great stress buster.'},
            {'name': 'Kitchen Chef Play Set', 'price': 799, 'compare_at_price': 1299, 'category': 'pretend-play', 'description': 'Realistic kitchen play set with utensils, stove and accessories.', 'is_featured': True},
            {'name': 'Doctor\'s Kit', 'price': 399, 'compare_at_price': 699, 'category': 'pretend-play', 'description': 'Pretend play doctor kit with stethoscope, syringe and medical tools.'},
            {'name': 'Birthday Return Gift Box (Set of 12)', 'price': 1499, 'compare_at_price': 2399, 'category': 'everyday-gifting', 'description': 'Pre-packed return gift boxes for 12 kids. Each box has toys and treats.', 'is_featured': True},
            {'name': 'Gift Hamper - Premium', 'price': 999, 'compare_at_price': 1599, 'category': 'everyday-gifting', 'description': 'Premium gift hamper with assorted toys, stationery and treats.'},
            {'name': 'Glass Water Bottle - Cartoon', 'price': 349, 'compare_at_price': 599, 'category': 'everyday-gifting', 'description': 'Cute cartoon glass water bottle with silicone sleeve.'},
            {'name': 'Coffee Mug - Quirky Design', 'price': 249, 'compare_at_price': 449, 'category': 'everyday-gifting', 'description': 'Ceramic coffee mug with fun quirky designs. Great gift for any occasion.'},
        ]

        created = 0
        for p in products:
            cat_slug = p.pop('category')
            cat = category_map.get(cat_slug)
            if not cat:
                self.stdout.write(self.style.WARNING(f'Category {cat_slug} not found, skipping {p["name"]}'))
                continue
            Product.objects.create(category=cat, **p)
            created += 1
        self.stdout.write(f'Created {created} products.')
