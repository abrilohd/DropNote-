from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("", views.note_list, name="index"),
    path("new/", views.note_create, name="create"),
    path("<int:pk>/", views.note_detail, name="detail"),
    path("<int:pk>/edit/", views.note_edit, name="edit"),
    path("<int:pk>/delete/", views.note_delete, name="delete"),
]