from django.contrib import admin

from . import models

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "prepare_time",
        "people",
    )

@admin.register(models.Baking)    
class BakingAdmin(admin.ModelAdmin):
    list_display = (
        'oven',
        'degrees',
    )

@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass