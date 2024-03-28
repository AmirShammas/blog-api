from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=50, null=False,
                             blank=False, verbose_name="Title")
    body = models.TextField(null=False, blank=False, verbose_name="Body")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("id",)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50, null=False,
                             blank=False, verbose_name="Title")
    body = models.TextField(null=False, blank=False, verbose_name="Body")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.PROTECT, related_name="posts", verbose_name="Author")
    category = models.ForeignKey(Category, null=False, blank=False, default=1,
                                 on_delete=models.PROTECT, related_name="posts", verbose_name="Category")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("id",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=50, null=False,
                             blank=False, verbose_name="Title")
    body = models.TextField(null=False, blank=False, verbose_name="Body")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.PROTECT, related_name="comments", verbose_name="Author")
    post = models.ForeignKey(Post, null=False, blank=False,
                             on_delete=models.PROTECT, related_name="comments", verbose_name="Post")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("id",)

    def __str__(self):
        return self.title
