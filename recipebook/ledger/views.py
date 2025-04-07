from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm

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
    ingredient_form = IngredientForm()
    recipe_ingredient_form = RecipeIngredientForm()
    if request.method == 'POST':
        if 'recipe' in request.POST:
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe_form.instance.author = request.user.profile
                recipe_form.save()
                return redirect('ledger:recipe_list')
        if 'ingredient' in request.POST:
            ingredient_form = IngredientForm(request.POST)
            if ingredient_form.is_valid():
                ingredient_form.save()
        if 'recipe_ingredient' in request.POST:
            recipe_ingredient_form = RecipeIngredientForm(request.POST)
            if recipe_ingredient_form.is_valid():
                recipe_ingredient_form.save()

    ctx = {'recipe_form':recipe_form, 
           'ingredient_form':ingredient_form, 
           'recipe_ingredient_form':recipe_ingredient_form}
    return render(request, 'recipe_maker.html', ctx)
