from django.shortcuts import render, HttpResponse
from ..models import Recipe, Baking
from .serializers import RecipeSerializer, BakingSerializer
from rest_framework import viewsets, permissions


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipe to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class BakingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Baking to be viewed or edited.
    """
    queryset = Baking.objects.all()
    serializer_class = BakingSerializer
