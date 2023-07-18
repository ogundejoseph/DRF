# from .views import PostList
# from rest_framework.routers import DefaultRouter

# app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='user')
# urlpatterns = router.urls


from django.urls import path
from .views import PostList, PostDetail, PostListDetailFilter

app_name = 'blog_api'

urlpatterns = [
    path('posts/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]
