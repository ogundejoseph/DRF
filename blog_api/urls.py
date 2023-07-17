
from django.urls import path
from .views import PostList, PostDetail, PostListDetailFilter

app_name = 'blog_api'

urlpatterns = [
    path('posts/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]
