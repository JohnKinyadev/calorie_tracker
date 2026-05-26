from django.test import TestCase

from .forms import FoodItemForm
from .models import FoodItem


class FoodItemModelTests(TestCase):
    def test_string_representation_includes_name_and_calories(self):
        item = FoodItem.objects.create(name='Banana', calories=105)

        self.assertEqual(str(item), 'Banana (105 kcal)')


class FoodItemFormTests(TestCase):
    def test_accepts_valid_food_item(self):
        form = FoodItemForm(data={'name': 'Rice', 'calories': 220})

        self.assertTrue(form.is_valid())

    def test_rejects_missing_name(self):
        form = FoodItemForm(data={'name': '', 'calories': 220})

        self.assertFalse(form.is_valid())
