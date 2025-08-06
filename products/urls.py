from . import signals

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .services.replenish_stock import admin_replenish_stock
from .views import ReviewViewSet, CategorViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'categories', CategorViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/replenish_stock/<int:product_id>/<int:amount>', admin_replenish_stock, name='admin_replenish_stock'),]