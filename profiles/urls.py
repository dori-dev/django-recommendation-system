"""profile urls
"""
from django.urls import path
from .views import my_recs_view

urlpatterns = [
    path('rec/', my_recs_view, name="my_recs"),
]
