# Generated by Django 4.1 on 2022-08-17 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_remove_video_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_reply',
        ),
    ]