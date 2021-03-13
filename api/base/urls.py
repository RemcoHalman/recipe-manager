from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from .api import views
from apps.recipe.api import views as recipe

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'recipe', recipe.RecipeViewSet)
router.register(r'baking', recipe.BakingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
