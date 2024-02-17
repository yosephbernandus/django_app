from django.urls import path

from web.homepage_app import views

urlpatterns = [
    path("", views.index, name="index"),
]