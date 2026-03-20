"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path, include

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

# Placeholder for api_root and router

from django.http import JsonResponse, HttpResponse
from django.urls import path

def landing_page(request):
    return HttpResponse('<h1>Welcome to Octofit Tracker!</h1><p>Your fitness journey starts here.</p>')

def api_root(request):
    return JsonResponse({'message': 'Octofit API Root'})

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
