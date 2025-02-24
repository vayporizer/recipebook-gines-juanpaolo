from django.urls import path
from .views import recipe_list, recipes

urlpatterns = [
    path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:num>/", recipes, name="recipes")
]