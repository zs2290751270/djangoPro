"""djangoPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from .serializers import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

api = [
    path('', include('race.member.urls')),
    path('', include('race.team.urls')),
    path('', include('iam.urls')),
    path('', include('jianlai.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify')

]

urlpatterns = [
    path('api/', include(api)),
    path('admin', admin.site.urls)
]
