from django.urls import path

from web.login_app import views

urlpatterns = [
    path("", views.index, name="index"),
]
