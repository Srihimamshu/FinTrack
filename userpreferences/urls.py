from django.urls import path
from . import views

urlpatterns = [
    path('', views.preferences, name='preferences'),
]
