# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
]
