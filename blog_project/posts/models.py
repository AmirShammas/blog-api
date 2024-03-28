from django.db import models
from django.conf import settings


class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name="Is Active",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    class Meta:
        abstract = True
        ordering = ("pk",)

    def __str__(self):
        raise NotImplementedError("Implement __str__ method")


class Category(MyBaseModel):
    title = models.CharField(max_length=50, null=False,
                             blank=False, verbose_name="Title")
    body = models.TextField(null=False, blank=False, verbose_name="Body")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("id",)

    def __str__(self):
        return self.title


class Post(MyBaseModel):
    title = models.CharField(max_length=50, null=False,
                             blank=False, verbose_name="Title")
    body = models.TextField(null=False, blank=False, verbose_name="Body")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.PROTECT, related_name="posts", verbose_name="Author")
    category = models.ForeignKey(Category, null=False, blank=False, default=4,
                                 on_delete=models.PROTECT, related_name="posts", verbose_name="Category")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("id",)

    def __str__(self):
        return self.title


class Comment(MyBaseModel):
    title = models.CharField(max_length=50, null=False,
                             blank=False, verbose_name="Title")
    body = models.TextField(null=False, blank=False, verbose_name="Body")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.PROTECT, related_name="comments", verbose_name="Author")
    post = models.ForeignKey(Post, null=False, blank=False,
                             on_delete=models.PROTECT, related_name="comments", verbose_name="Post")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("id",)

    def __str__(self):
        return self.title
