from django.urls import path, include
from .endpoint import views, auth_views


urlpatterns = [
    path('', auth_views.google_login)
]