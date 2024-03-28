from django.contrib import admin
from .models import Category, Comment, Post
from django.contrib.admin import register

# admin.site.register(Post)


@admin.action(description="Activate selected items")
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Inactivate selected items")
def inactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


class PostInline(admin.StackedInline):
    model = Post
    extra = 1


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "is_active",)
    list_display_links = ("id", "title",)
    list_filter = ("category", "is_active", "created_at",)
    list_editable = ("is_active",)
    search_fields = ("title", "body",)
    actions = (activate_selected_items, inactivate_selected_items)
    inlines = (CommentInline,)


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "post", "is_active",)
    list_display_links = ("id", "title",)
    list_filter = ("post", "is_active", "created_at",)
    list_editable = ("is_active",)
    search_fields = ("body",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active",)
    list_display_links = ("id", "title",)
    list_filter = ("is_active", "created_at", "updated_at")
    list_editable = ("is_active",)
    search_fields = ("title",)
    actions = (activate_selected_items, inactivate_selected_items)
    inlines = (PostInline,)
