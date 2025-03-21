from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(required=False, allow_null=True)  # Make image field optional

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'image', 'tags', 'category', 'created_at', 'updated_at')
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('post',)