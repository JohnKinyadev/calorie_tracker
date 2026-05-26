from django.db import models
from cloudinary.models import CloudinaryField


class FoodItem(models.Model):
    """A food item consumed by the user with a calorie value and timestamp."""

    name = models.CharField(max_length=150)
    calories = models.PositiveIntegerField()
    image = CloudinaryField('image', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.name} ({self.calories} kcal)'
