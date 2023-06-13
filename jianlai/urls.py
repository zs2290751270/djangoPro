
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('api/wsb', views.WsbView)

urlpatterns = [
    path('', include(router.urls)),
]

