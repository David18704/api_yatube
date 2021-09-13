from rest_framework import serializers
from posts.models import Group, Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "pub_date")


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=False,
    )

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
        read_only_fields = ('post',)
