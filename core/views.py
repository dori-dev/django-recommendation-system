"""core views
"""
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from profiles.models import Profile


def index_view(request: WSGIRequest, code: str = False):
    if code:
        profile = Profile.objects.filter(code=code)
        if profile.exists():
            request.session['code'] = profile[0].id
    return render(request, 'index.html', {})
