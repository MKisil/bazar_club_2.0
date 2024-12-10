from django.db import models
from cities_light.models import Region


class JobPostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')

    def __str__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    publication_date = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salary')
    days_per_week = models.PositiveIntegerField(verbose_name='Number days')
    hours_per_day = models.CharField(max_length=20, verbose_name='Daily hours')
    category = models.ForeignKey(JobPostCategory, on_delete=models.CASCADE, verbose_name='Category')

    def __str__(self):
        return self.title


class HousingPostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='housing_posts/other_images/', blank=True, verbose_name='Image')

    def __str__(self):
        return f"Image {self.id}"


class HousingPost(models.Model):
    TYPE_CHOICES = [
        ('vip', 'VIP'),
        ('super_vip', 'Super VIP'),
        ('premium', 'Premium'),
    ]
    main_image = models.ImageField(upload_to='housing_posts/main_images/', verbose_name='Main image')
    title = models.CharField(max_length=255, verbose_name='Title')
    location = models.CharField(max_length=255, verbose_name='Location')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Type')
    short_description = models.TextField(verbose_name='Short description')
    other_images = models.ManyToManyField(Image, related_name='housing_posts', verbose_name='Other images')
    living_conditions = models.TextField(verbose_name='Living conditions')
    category = models.ForeignKey(HousingPostCategory, on_delete=models.CASCADE, verbose_name='Category')

    def __str__(self):
        return self.title