from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("posts/", views.post_list),
    path("posts_detail", views.post_detail),
    path("posts_add/", views.post_add),
]