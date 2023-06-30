from django.urls import path
from rest_framework.routers import DefaultRouter

from tasks.views import TasksViewSet

router = DefaultRouter()
router.register("tasks", TasksViewSet)

urlpatterns = router.urls
