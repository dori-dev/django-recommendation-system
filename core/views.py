"""core views
"""
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from profiles.models import Profile


def signup_view(request: WSGIRequest):
    return render(request, 'signup.html', {})


def index_view(request: WSGIRequest, code: str = None):
    if code:
        profile = Profile.objects.filter(code=code)
        if profile.exists:
            request.session['code'] = profile[0].id
    print(request.session)
    print(request.session.get_expiry_age())
    return render(request, 'index.html', {})
