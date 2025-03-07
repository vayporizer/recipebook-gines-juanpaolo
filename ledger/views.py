from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'