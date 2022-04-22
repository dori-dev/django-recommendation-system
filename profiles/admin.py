from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ["code"]
    list_display = ["user", "code", "recommended_by"]
    list_filter = ["recommended_by"]


admin.site.register(Profile, ProfileAdmin)
