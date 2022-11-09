from django.db import models

# Create your models here.
class Stage(models.Model):
    stage_level = models.CharField(max_length=10, primary_key=True)
    stage_map = models.CharField(max_length=3000)
    stage_hint = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)