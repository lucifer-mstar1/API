from django.contrib import admin
from django.urls import path, include
from billing.views import CreateChargeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/pay/', CreateChargeView.as_view(), name='create-charge'),
]
