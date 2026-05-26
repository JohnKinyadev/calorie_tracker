from django.shortcuts import get_object_or_404, redirect, render

from .forms import FoodItemForm
from .models import FoodItem
from .services import calculate_total_calories, get_today_items


def dashboard(request):
    items = get_today_items()
    total_calories = calculate_total_calories(items)
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
