# from rest_framework import generics, permissions
from .models import Comment, Post
from .serializers import CommentCreateSerializer, CommentSerializer, CommentUpdateSerializer, PostCreateSerializer, PostSerializer, PostUpdateSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .pagination import CustomPagination


"""
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
"""


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'update':
            return PostUpdateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    """
    def get_queryset(self):
        author_id = self.request.query_params.get('author')
        if author_id:
            return Post.objects.filter(author_id=author_id)
        return Post.objects.all()
    """

    def get_queryset(self):
        author_username = self.request.query_params.get('author')
        if author_username:
            author = get_user_model().objects.filter(username=author_username).first()
            if author:
                return Post.objects.filter(author=author, is_active=True)
        # return Post.objects.all()
        return Post.objects.filter(is_active=True)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = CommentSerializer
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        elif self.action == 'update':
            return CommentUpdateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        author_username = self.request.query_params.get('author')
        post_id = self.request.query_params.get('post')
        if author_username:
            author = get_user_model().objects.filter(username=author_username).first()
            if author:
                return Comment.objects.filter(author=author, is_active=True)
        elif post_id:
            post = Post.objects.filter(id=post_id).first()
            if post:
                return Comment.objects.filter(post=post, is_active=True)
        return Comment.objects.filter(is_active=True)
