from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=255)
    top_score = models.IntegerField(default=0)
    top_accuracy = models.IntegerField(default=0)