from django.urls import re_path
from .views import *


urlpatterns = [
    re_path('^api/iam/$', Iam.as_view()),
    re_path('^api/iam/(?P<pk>[\\w_-]+)/$', IamDetail.as_view()),
    re_path('^api/permission/(?P<pk>[\\w_-]+)/$', PermissionM.as_view()),
]
