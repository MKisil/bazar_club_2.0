from rest_framework import serializers
from .models import JobPost, JobPostCategory, HousingPostCategory, Image, HousingPost


class JobPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostCategory
        fields = '__all__'

class JobPostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=JobPostCategory.objects.all())
    class Meta:
        model = JobPost
        fields = '__all__'

class HousingPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingPostCategory
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class HousingPostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=HousingPostCategory.objects.all())
    class Meta:
        model = HousingPost
        fields = '__all__'