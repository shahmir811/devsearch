from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),

    
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>/", views.user_profile, name="user-profile"),
    path("account/", views.user_account, name="user-account"),
    path("edit-account/", views.edit_account, name="edit-account"),
    path("create-skill/", views.create_skill, name="create-skill"),
    path("update-skill/<str:pk>/", views.update_skill, name="update-skill"),
    path("delete-skill/<str:pk>/", views.delete_skill, name="delete-skill"),
]
