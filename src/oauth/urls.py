from django.urls import path, include
from .endpoint import views, auth_views


urlpatterns = [
    path('google/', auth_views.google_auth),
    path('', auth_views.google_login),

]