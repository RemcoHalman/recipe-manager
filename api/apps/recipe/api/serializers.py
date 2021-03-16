from ..models import Recipe, Ingredient, Baking, Food
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class BakingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baking
        fields = '__all__'

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'