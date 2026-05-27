# Calorie Counter

A small Django app for logging daily food items and tracking the total calories for the current day.

## Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Environment

Copy `.env.example` to `.env` and update the values for your machine or hosting provider.
The app uses SQLite by default, and `DATABASE_URL` can point to PostgreSQL in production.

## Usage

Open the dashboard, add each food item with its calorie count, and use the remove or reset controls to manage today's log.

## Tests

```powershell
python manage.py test
```

## Deployment

The project pins Python with `.python-version` because Django 4.2 supports Python up to 3.12.
On Render, make sure the service root directory points at this Django project folder so Render can read `.python-version` before building.

Set `DJANGO_DEBUG=False`, provide a strong `DJANGO_SECRET_KEY`, configure `DJANGO_ALLOWED_HOSTS`, and point `DATABASE_URL` at the production database before deploying.
Keep Cloudinary credentials in environment variables: `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET`.
