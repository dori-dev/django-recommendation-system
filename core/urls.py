"""core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('auth/', include('auth.urls')),
    path('profile/', include('profiles.urls')),
    path('<str:code>/', index_view, name='index'),
]
