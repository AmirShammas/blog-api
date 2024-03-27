from rest_framework import serializers
from .models import Category, Comment, Post
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "post",
            "title",
            "body",
            "created_at",
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "title", "body",)


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("title", "body",)


class PostSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "category",
            "title",
            "body",
            "created_at",
            "comments",
        )

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("category", "title", "body",)


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("category", "title", "body",)


class CategorySerializer(serializers.ModelSerializer):

    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "body",
            "created_at",
            "posts",
        )
    
    def get_posts(self, obj):
        posts = Post.objects.filter(category=obj)
        serializer = PostSerializer(posts, many=True)
        return serializer.data


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "body",)


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "body",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)
