from django.urls import path
from .views import PostListCreateView, PostDetailView,CommentDetailView,CommentListCreateView,LikePostView,BookmarkPostView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:post_id>/bookmark/', BookmarkPostView.as_view(), name='bookmark-post'),
]