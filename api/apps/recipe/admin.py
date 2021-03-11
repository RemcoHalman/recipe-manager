from django.contrib import admin

from . import models

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Baking)    
class BakingAdmin(admin.ModelAdmin):
    list_display = (
        'recipe',
        'oven',
        'degrees',
    )
