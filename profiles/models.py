from django.db import models
from django.contrib.auth.models import User
from .utils import generate_code


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=256, blank=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User,
                                       on_delete=models.CASCADE,
                                       blank=True, null=True,
                                       related_name='recommended')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_recommended_profiles(self):
        pass

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_code()
            self.code = code
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
