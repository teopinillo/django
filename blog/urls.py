from django.urls import path
from .views import (likedPost, 
BlogUpdateView,
BlogListView,
BlogDetailView,
login_view,
logout_view,
register,
about,
index,
delete_post,
show404)

urlpatterns = [ 
    #path ('', BlogListView.as_view(), name = 'index'),
    path ('', index, name = 'index'),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("register", register, name="register"),
    path("about", about, name="about"),
    path("likedpost/<int:postid>", likedPost, name="likedpost"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name = 'post_edit'),   #11/18/2021
    path("post/<int:pk>/delete/", delete_post, name = 'post_delete'),   #11/21/2021
    path("404", show404, name="show404"),

]
