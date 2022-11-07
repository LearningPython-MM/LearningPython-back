from django.contrib import admin
from .models import UserInfo, Record, Rank

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Record)
admin.site.register(Rank)