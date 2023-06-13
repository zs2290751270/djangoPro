from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import MemberViewSet

router = DefaultRouter()
router.register('race/member', MemberViewSet)

urlpatterns = [
    path('', include(router.urls))
]


