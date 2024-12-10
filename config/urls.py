"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from src.apps.posts.views import JobPostViewSet, JobPostCategoryViewSet, ImageViewSet, HousingPostViewSet

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'jobpostcategory', JobPostCategoryViewSet, basename='jobpostcategory')
router.register(r'jobposts', JobPostViewSet, basename='jobpost')
router.register(r'image', ImageViewSet, basename='image')
router.register(r'housingpostcategory', HousingPostViewSet, basename='housingpostcategory')
router.register(r'housingposts', HousingPostViewSet, basename='housingpost')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('src.apps.users.urls')),
    # path('users/social/', include('allauth.urls')),
    # path('users/social/', include('allauth.socialaccount.urls')),
    path('api/posts/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)