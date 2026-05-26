from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('remove/<int:item_id>/', views.remove_food_item, name='remove_food_item'),
]
