from django.urls import path, include
from . import views


urlpatterns = [
    path('genre/', views.GenreView.as_view()),

    path


]