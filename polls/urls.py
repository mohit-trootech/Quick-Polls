# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("vote", views.vote, name="vote"),
    path("add", views.PollsCreate.as_view(), name="polls-create"),
    path("info", views.PollsInfo.as_view(), name="info"),
]
