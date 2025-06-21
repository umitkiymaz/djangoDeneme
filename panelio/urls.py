from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Giriş, çıkış, şifre yönetimi
    path('', include('main.urls')),
]
