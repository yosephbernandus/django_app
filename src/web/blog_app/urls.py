from django.urls import path

from web.blog_app import views

urlpatterns = [
    path("", views.index, name="index"),
]