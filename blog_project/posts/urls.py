from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail


urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
]
