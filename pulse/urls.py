from django.urls import path
from . import views

app_name = 'pulse'

urlpatterns = [
    path('feed/', views.feed_view, name='feed'),
    path('upload_pulse', views.upload_pulse_view, name='upload_pulse'),
]
