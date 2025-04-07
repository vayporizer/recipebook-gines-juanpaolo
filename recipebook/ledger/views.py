from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def recipe(request, key):
    recipe = Recipe.objects.get(id=key)
    return render(request, 'recipe.html', {'recipe': recipe})

@login_required
def recipe_maker(request):
    recipe_form = RecipeForm()
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user.profile
            recipe_form.save()
            return redirect('ledger:recipe_list')
    return render(request, 'recipe_maker.html', {'recipe_form':recipe_form})
