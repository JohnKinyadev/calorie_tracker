from django.test import TestCase
from django.urls import reverse

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


class DashboardViewTests(TestCase):
    def test_dashboard_renders_total_calories(self):
        FoodItem.objects.create(name='Oats', calories=180)
        FoodItem.objects.create(name='Eggs', calories=140)

        response = self.client.get(reverse('tracker:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '320 kcal')

    def test_dashboard_adds_food_item(self):
        response = self.client.post(
            reverse('tracker:dashboard'),
            {'action': 'add', 'name': 'Beans', 'calories': 300},
        )

        self.assertRedirects(response, reverse('tracker:dashboard'))
        self.assertTrue(FoodItem.objects.filter(name='Beans').exists())

    def test_dashboard_resets_food_items(self):
        FoodItem.objects.create(name='Tea', calories=40)

        response = self.client.post(reverse('tracker:dashboard'), {'action': 'reset'})

        self.assertRedirects(response, reverse('tracker:dashboard'))
        self.assertEqual(FoodItem.objects.count(), 0)
