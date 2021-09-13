from django.urls import include, path

from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
