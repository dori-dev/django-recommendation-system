"""core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from .views import index_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
    path('rec/', include('profiles.urls'), name='my_rec'),
    path('<str:code>/', index_view, name='index'),
]
