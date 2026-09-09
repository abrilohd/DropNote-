from django.contrib import admin
from django.urls import include, path

from notes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("notes/", include("notes.urls")),
]
