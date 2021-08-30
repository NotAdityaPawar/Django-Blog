from django.urls import path
from .views import PostListView,PostDetailView, PostCreateView


urlpatterns = [
    path("",PostListView.as_view(),name = "list"),
    path("post/<int:pk>",PostDetailView.as_view(),name = "detail"),
    path("add_post/",PostCreateView.as_view(),name = "add_post")
]
