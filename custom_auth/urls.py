# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),                      # /auth/users/ (register)
    path('auth/', include('djoser.urls.jwt')),                  # /auth/jwt/create/ (login)
]
