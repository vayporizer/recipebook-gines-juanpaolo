from django.urls import path
from .views import recipe_list, RecipeDetailView

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe')
]

app_name = 'ledger'