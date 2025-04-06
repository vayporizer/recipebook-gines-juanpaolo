from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.name)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=10)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    
    def __str__(self):
        return '{} of {} in {}'.format(self.quantity, self.ingredient.name, self.recipe.name)
    
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return '{} Image'.format(self.recipe.name)
    