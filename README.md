# Tiny Town Creations — Backend

Django REST API for [Tiny Town Creations](https://tinytowncreations.in), an e-commerce store for kids' toys, return gifts, and novelty items.

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6 + Django REST Framework |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Media | Cloudinary (with local fallback) |
| Auth | Django Admin (no public auth) |

## Project Structure

```
tiny_town_backend/
├── config/               # Django project settings, URLs, WSGI/ASGI
├── apps/
│   ├── categories/       # Categories (hierarchical) & Tags
│   ├── products/         # Products, images, videos, filtering
│   └── store_config/     # Store info, testimonials, banners, reels, locations
├── media/                # Local media storage (fallback)
├── manage.py
└── requirements.txt
```

## API Endpoints (all read-only, `/api/v1/`)

| Endpoint | Description |
|---|---|
| `categories/` | List/filter categories (top-level with `?top_level=true`) |
| `categories/{slug}/` | Category detail with children |
| `products/` | List/filter products (by `category`, `tag`, `min_price`, `max_price`, `is_featured`, `age_range`) |
| `products/{slug}/` | Product detail with images, videos, related products |
| `config/` | Store config (name, social links, hero, announcement, SEO) |
| `testimonials/` | Customer reviews |
| `banners/` | Time-aware banners (filter by `position`: hero/announcement/promo) |
| `reels/` | Instagram reels |
| `locations/` | Serviceable cities/areas |

## Setup

### Prerequisites

- Python 3.11+
- pip

### 1. Clone & enter

```bash
git clone <repo-url>
cd tiny_town_backend
```

### 2. Virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment variables

Copy the template below into `.env` (most values have safe defaults):

```env
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000

# Cloudinary (optional — leave defaults for local media)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Seed data (optional)

```bash
python manage.py seed_categories
python manage.py seed_data          # testimonials, locations, reels, sample products
```

### 7. Start server

```bash
python manage.py runserver
```

Visit **http://localhost:8000/admin/** (create a superuser first with `python manage.py createsuperuser`) or hit the API at **http://localhost:8000/api/v1/**.

## Admin

All data mutations go through the Django admin. Create a superuser:

```bash
python manage.py createsuperuser
```
# tiny_town_backend
# tiny_town_BE
# tiny_town_backend
