from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]
    ('Details', {'ingredients':('name', 'quantity')})
    list_display = ('name', 'author', 'created_on', 'updated_on')
    search_fields = ('name',)
    list_filter = ('name', 'author', 'created_on', 'updated_on')

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity')
    search_fields = ('recipe__name', 'ingredient__name')
    list_filter = ('recipe', 'ingredient')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
