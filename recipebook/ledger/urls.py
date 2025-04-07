from django.urls import path
from .views import recipe_list, recipe, recipe_maker

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:key>/', recipe, name='recipe'),
    path('recipe/add/', recipe_maker, name='recipe_maker')
]

app_name = 'ledger'
