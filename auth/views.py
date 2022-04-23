"""auth views
"""
from django.shortcuts import redirect, render
from django.db.models.query import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from profiles.models import Profile


def signup_view(request: WSGIRequest):
    profile_id = request.session.get('code')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if profile_id is not None:
                rec_by_profile: QuerySet[Profile] = Profile.objects.filter(
                    id=profile_id)
                if rec_by_profile.exists():
                    user: User = form.save()
                    registered_user = User.objects.get(id=user.id)
                    registered_profile: Profile = Profile.objects.get(
                        user=registered_user)
                    registered_profile.recommended_by = rec_by_profile[0].user
                    registered_profile.save()
            else:
                user = form.save()
            login(request, user)
            return redirect("my_recs")
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
