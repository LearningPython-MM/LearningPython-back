# Generated by Django 4.1.3 on 2022-12-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rank_created_at_rank_updated_at_record_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]