from django.urls import path
from accounts.views import LoginView, RegisterView


"""
URL routes for Accounts App
"""

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]