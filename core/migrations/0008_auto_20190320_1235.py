# Generated by Django 2.1.7 on 2019-03-20 16:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190320_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
