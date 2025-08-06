from django.contrib import admin
from django.urls import path, include, re_path
from billing.views import CreateChargeView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.contrib.auth import views as auth_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v1',
      description="API for Ecommerce app",
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
    path('api/v1/custom_auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/custom_auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/custom_auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/pay/', CreateChargeView.as_view(), name='create-charge'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # login/logout if required
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Swagger & ReDoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
