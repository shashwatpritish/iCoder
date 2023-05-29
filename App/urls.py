from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("addpost/", views.addpost, name="AddPost"),
    path("posts/", views.posts, name="Post"),
    path("posts/<str:slug>", views.blog, name="Blog"),
    path("delete/<str:slug>", views.delete, name="Delete"),
    path("contact/",  views.contact, name="Contact"),
    path("about/", views.about, name="about")
]