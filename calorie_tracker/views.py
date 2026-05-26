from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import FoodItemForm
from .models import FoodItem


def get_today_items():
    today = timezone.localdate()
    return FoodItem.objects.filter(created_at__date=today)


def dashboard(request):
    items = get_today_items()
    total_calories = sum(item.calories for item in items)
    form = FoodItemForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get('action') == 'add' and form.is_valid():
            form.save()
            return redirect('tracker:dashboard')

        if request.POST.get('action') == 'reset':
            items.delete()
            return redirect('tracker:dashboard')

    return render(
        request,
        'calorie_tracker/index.html',
        {
            'form': form,
            'items': items,
            'total_calories': total_calories,
        },
    )


def remove_food_item(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('tracker:dashboard')
