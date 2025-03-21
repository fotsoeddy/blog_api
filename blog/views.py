from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.author == self.request.user:
            serializer.save()
        else:
            raise serializers.ValidationError("You are not the author of this post.")

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        else:
            raise serializers.ValidationError("You are not the author of this post.")
        
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = generics.get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.author == self.request.user:
            serializer.save()
        else:
            raise serializers.ValidationError("You are not the author of this comment.")

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        else:
            raise serializers.ValidationError("You are not the author of this comment.")
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Like

class LikePostView(generics.CreateAPIView, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        post = generics.get_object_or_404(Post, id=post_id)
        Like.objects.get_or_create(post=post, user=request.user)
        return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        post = generics.get_object_or_404(Post, id=post_id)
        Like.objects.filter(post=post, user=request.user).delete()
        return Response({"message": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)
    
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'author__username']
    search_fields = ['title', 'content', 'tags']
class BookmarkPostView(generics.CreateAPIView, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        post = generics.get_object_or_404(Post, id=post_id)
        Bookmark.objects.get_or_create(post=post, user=request.user)
        return Response({"message": "Post bookmarked."}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        post = generics.get_object_or_404(Post, id=post_id)
        Bookmark.objects.filter(post=post, user=request.user).delete()
        return Response({"message": "Post unbookmarked."}, status=status.HTTP_204_NO_CONTENT)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'author__username']  # Filter by category or author
    search_fields = ['title', 'content', 'tags']  # Search by title, content, or tags

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

