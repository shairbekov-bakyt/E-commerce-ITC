from rest_framework.routers import DefaultRouter

from tracker import views


router = DefaultRouter()
router.register("task", views.TaskViewSet)


urlpatterns = router.urls
