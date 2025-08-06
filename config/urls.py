from django.contrib.auth import views as auth_views  # 👈 Add this
from django.contrib import admin
from django.urls import path, include
from billing.views import CreateChargeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),

    path('api/v1/custom_auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/custom_auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/custom_auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/pay/', CreateChargeView.as_view(), name='create-charge'),

    # ✅ ADD these lines to fix the 404 for /accounts/login/
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Swagger + ReDoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
