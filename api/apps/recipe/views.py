from django.shortcuts import render, HttpResponse
from .models import Recipe, Baking
from .serializers import RecipeSerializer, BakingSerializer
from rest_framework import viewsets, permissions


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipe to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
