from django.urls import path

from . import views

urlpatterns = [
    path("", views.projects, name="projects"),
    # path("str:<pk>/", views.project, name="single-project"),
    path("create-project/", views.create_project, name="create-project"),
    path("update-project/<str:pk>", views.update_project, name="update-project"),
    path("delete-project/<str:pk>", views.delete_project, name="delete-project"),
    path("<str:pk>/", views.project, name="single-project"),  # Corrected this line
]
