from django.urls import path
from . import views

urlpatterns = [
    path('send-sync/', views.handle_user_data_sync),
    path('send-async/', views.handle_user_data_async),
]