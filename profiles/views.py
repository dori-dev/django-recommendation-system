from django.shortcuts import render
from .models import Profile


def my_recs_view(request):
    """TODO"""
    print(request.user)  # TODO for no signup user
    profile: Profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profiles()
    context = {
        "my_recs": my_recs,
    }
    return render(request, 'profiles/recommendations.html', context)
