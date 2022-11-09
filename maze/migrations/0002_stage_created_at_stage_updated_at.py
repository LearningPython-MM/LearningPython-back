# Generated by Django 4.1.3 on 2022-11-09 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
