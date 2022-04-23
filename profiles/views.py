"""profile views
"""
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required(login_url="signup")
def my_recs_view(request):
    """TODO"""
    print(request.user)  # TODO for no signup user
    profile: Profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profiles()
    code = reverse("index", kwargs={"code": str(profile.code)})
    context = {
        "my_recs": my_recs,
        "code": code,
    }
    return render(request, 'profiles/recommendations.html', context)
