from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def recipe(request, key):
    recipe = Recipe.objects.get(id=key)
    return render(request, 'recipe.html', {'recipe': recipe})
