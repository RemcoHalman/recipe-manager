from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from .api import views
from apps.recipe.api import views as recipe

router = routers.DefaultRouter()
# Default models
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# Recipe App routes
router.register(r'recipe', recipe.RecipeViewSet)
router.register(r'ingredienten', recipe.IngredientViewSet)
router.register(r'baking', recipe.BakingViewSet)
router.register(r'food', recipe.FoodViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
