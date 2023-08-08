from django.db import models


# Create your models here.
class AwsBucketModel(models.Model):
    name = models.CharField(max_length=300)
    link = models.CharField(max_length=600)
    file = models.CharField(max_length=300)

