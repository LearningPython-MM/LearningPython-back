from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_id = models.CharField(max_length=5, primary_key=True)
    user_pw = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Record(models.Model):
    record_num = models.IntegerField( primary_key=True)
    user_id = models.CharField(max_length=5)
    stage_level = models.IntegerField()
    record_code = models.CharField(max_length=3000)
    record_complexity = models.IntegerField()
    record_time = models.CharField(max_length=20)
    record_date = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rank(models.Model):
    user_id = models.CharField(max_length=5, primary_key=True)
    stage_level = models.IntegerField()
    rank_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)