from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "code", "recommended_by"]


admin.site.register(Profile, ProfileAdmin)
