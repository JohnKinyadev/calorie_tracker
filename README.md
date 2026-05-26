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
