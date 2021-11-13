from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from blog.api.views import CommentViewSet

from library.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("comments", CommentViewSet)


app_name = "api"
urlpatterns = router.urls
