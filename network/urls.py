
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_post", views.add_post, name="add_post"),
    path("profile/<str:person>", views.profile, name="profile"),
    path("following", views.following, name="following"),
    path("profile/follow/<str:person>", views.follow, name="follow"),
    path("profile/unfollow/<str:person>", views.unfollow, name="unfollow"),
    path("posts/<int:post_id>", views.view_post, name="view_post"),
    path("add_comment", views.add_comment, name="add_comment"),
    
    #API routes
    path("edit/post_<int:post_id>", views.edit_post, name="edit_post"),
    path("like/post_<int:post_id>", views.like_post, name="like_post"),
    path("unlike/post_<int:post_id>", views.unlike_post, name="unlike_post"),
]
