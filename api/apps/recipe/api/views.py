from django.shortcuts import render, HttpResponse
from ..models import (
    Recipe,
    Ingredient,
    Baking,
    Food, 
)
from .serializers import (
    RecipeSerializer,
    IngredientSerializer,
    BakingSerializer,
    FoodSerializer
)
from rest_framework import viewsets, permissions



class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipe to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredient to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class BakingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Baking to be viewed or edited.
    """
    queryset = Baking.objects.all()
    serializer_class = BakingSerializer

class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Food to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
