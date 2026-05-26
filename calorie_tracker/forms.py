from django import forms

from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    """Form for submitting a new food item to the calorie tracker."""

    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'w-full rounded border border-slate-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200',
                    'placeholder': 'Enter food item',
                }
            ),
            'calories': forms.NumberInput(
                attrs={
                    'class': 'w-full rounded border border-slate-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200',
                    'placeholder': 'Calories',
                    'min': '0',
                }
            ),
        }
