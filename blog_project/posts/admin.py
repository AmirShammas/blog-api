from django.contrib import admin
from .models import Post
from django.contrib.admin import register

# admin.site.register(Post)


@admin.action(description="Activate selected items")
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Inactivate selected items")
def inactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "is_active",)
    list_editable = ("is_active",)
    actions = (activate_selected_items, inactivate_selected_items)
