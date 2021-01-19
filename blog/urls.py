from django.urls import path
from .views import likedPost, BlogListView, BlogDetailView, login_view, logout_view, register, about, new_post, index

urlpatterns = [ 
    #path ('', BlogListView.as_view(), name = 'index'),
    path ('', index, name = 'index'),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("register", register, name="register"),
    path("about", about, name="about"),
    path("likedpost/<int:postid>", likedPost, name="likedpost"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    #path("new_post", new_post, name="new_post"),   #11/18/2021

]
