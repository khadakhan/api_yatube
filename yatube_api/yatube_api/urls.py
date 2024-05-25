from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views


from api.views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register(r'api/v1/posts/(?P<post_id>.+?)/comments', CommentViewSet,
                basename='comment')


urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
