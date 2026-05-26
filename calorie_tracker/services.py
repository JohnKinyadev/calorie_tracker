from django.utils import timezone

from .models import FoodItem


def get_today_items():
    today = timezone.localdate()
    return FoodItem.objects.filter(created_at__date=today)


def calculate_total_calories(items):
    return sum(item.calories for item in items)
