from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import TeamViewSet

router = DefaultRouter()
router.register('race/team', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


