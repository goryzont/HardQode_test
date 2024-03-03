from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hardqode import views
from hardqode.views import ProductViewSet, LessonViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'lessons/(?P<product_id>\d+)', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]