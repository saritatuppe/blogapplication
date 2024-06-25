from django.urls import path
#from . import views
from . views import (
  PostListView,
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView
)

urlpatterns = [
  #path('',view.home,name="home")
  path('',PostListView.as_view(),name="home"),
  path('post/<int:pk>',PostDetailView.as_view(),name="post-detail"),
  path('post/new',PostCreateView.as_view(),name="post-create"),
  path('post/<int:pk>/update',PostUpdateView.as_view(),name="post-update"),
  path('post/<int:pk>/delete',PostDeleteView.as_view(),name="post-delete"),
]

