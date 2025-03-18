from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]
    ('Details', {
        'ingredients':
        ('name', 'quantity')
    })
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity')  
    search_fields = ('recipe__name', 'ingredient__name')
    list_filter = ('recipe', 'ingredient')  

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)