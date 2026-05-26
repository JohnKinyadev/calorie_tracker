from django.test import TestCase

from .models import FoodItem


class FoodItemModelTests(TestCase):
    def test_string_representation_includes_name_and_calories(self):
        item = FoodItem.objects.create(name='Banana', calories=105)

        self.assertEqual(str(item), 'Banana (105 kcal)')
