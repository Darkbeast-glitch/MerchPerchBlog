# Generated by Django 4.0.1 on 2022-01-11 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
