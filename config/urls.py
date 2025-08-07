from django.urls import path
from .views import RegisterView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
    
    # 🔐 JWT Authentication
    path('api/v1/custom_auth/', include('custom_auth.urls')),  # <-- added this
    path('api/v1/custom_auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/custom_auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/custom_auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # 💳 Billing
    path('api/v1/pay/', CreateChargeView.as_view(), name='create-charge'),

    # 🔍 Swagger & Docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # 👤 (Optional) Django default login
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Root Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
