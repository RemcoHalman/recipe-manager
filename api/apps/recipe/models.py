from django.db import models

OVEN_CHOICES = (
    ('hetelucht','Hetelucht'),
    ('bovenonder', 'Boven- en onderwarmte'),
)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    prepare_time = models.IntegerField(help_text="Bereidingstijd in minuten")
    people = models.IntegerField(help_text="Aantal personen")

    def __str__(self):
        return self.name
    

class Baking(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    oven = models.CharField(max_length=10, choices=OVEN_CHOICES, default='hetelucht')
    degrees = models.IntegerField(help_text="Hoeveelheid graden")
    oven_time = models.DurationField(help_text="Tijdsduur in de oven hh:mm:ss")

    def __str__(self):
        return self.recipe
    
# Create your models here.
# Baking
# Food
# Ingredients