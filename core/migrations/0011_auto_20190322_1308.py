# Generated by Django 2.1.7 on 2019-03-22 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_added']},
        ),
    ]