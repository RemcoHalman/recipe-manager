from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50, verbose_name=('Recipe | name'))
    prepare_time = models.IntegerField(help_text="Bereidingstijd in minuten")
    people = models.IntegerField(help_text="Aantal personen")

    def __str__(self):
        return self.name
    

class Baking(Recipe):
    """Extends Recipe Base model"""
    OVEN_CHOICES = (
        ('hetelucht','Hetelucht'),
        ('bovenonder', 'Boven- en onderwarmte'),
    )
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    oven = models.CharField(max_length=10, choices=OVEN_CHOICES, default='hetelucht', verbose_name="Oven stand")
    degrees = models.IntegerField(help_text="Hoeveelheid graden", verbose_name=('Graden'))
    oven_time = models.TimeField(help_text="Tijdsduur in de oven hh:mm:ss")

    def __str__(self):
        return self.name

class Food(Recipe):
    """Extends Recipe Base model"""
    detail = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    VOLUME_CHOICES = (
        ('gr','Gram'),
        ('ml', 'Milliliter'),
        ('l', 'Liter'),
        ('el', 'Eetlepel'),
        ('tl', 'Theelepel'),
    )
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name=('Ingredient | name'))
    amount = models.FloatField(null=True, blank=True, verbose_name=('Ingredient | amount'))
    volume = models.CharField(max_length=10, choices=VOLUME_CHOICES, default='gr', verbose_name="Amount | Type")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    prep_method = models.TextField(blank=True)

# Create your models here.
# Baking
# Food
# Ingredients