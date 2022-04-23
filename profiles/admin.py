"""profiles admin
"""
from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ["code"]
    list_display = ["user", "code", "recommended_by", "count"]
    list_filter = ["recommended_by"]

    @admin.display(description="recommended count")
    def count(self, model: Profile):
        return Profile.objects.filter(
            recommended_by=model.user
        ).count()


admin.site.register(Profile, ProfileAdmin)
