from django.shortcuts import render
from rest_framework import viewsets
from .models import JobPostCategory, JobPost, HousingPostCategory, Image, HousingPost
from .serializers import JobPostCategorySerializer, JobPostSerializer, HousingPostCategorySerializer, ImageSerializer, HousingPostSerializer


class JobPostCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobPostCategory.objects.all()
    serializer_class = JobPostCategorySerializer

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class HousingPostCategoryViewSet(viewsets.ModelViewSet):
    queryset = HousingPostCategory.objects.all()
    serializer_class = HousingPostCategorySerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class HousingPostViewSet(viewsets.ModelViewSet):
    queryset = HousingPost.objects.all()
    serializer_class = HousingPostSerializer