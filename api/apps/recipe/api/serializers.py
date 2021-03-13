from ..models import Recipe, Baking
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'prepare_time', 'people']


class BakingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baking
        fields = [
            'recipe',
            'oven',
            'degrees',
            'oven_time'
        ]
