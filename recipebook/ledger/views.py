from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe(request, key):
    recipe = Recipe.objects.get(id=key)
    return render(request, 'recipe.html', {'recipe': recipe})
