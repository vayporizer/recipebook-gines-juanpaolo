from django import forms
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
