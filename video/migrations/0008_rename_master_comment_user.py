# Generated by Django 4.1 on 2022-08-16 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_alter_comment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='master',
            new_name='user',
        ),
    ]