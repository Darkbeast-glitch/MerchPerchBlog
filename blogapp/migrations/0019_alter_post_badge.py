# Generated by Django 3.2.4 on 2022-05-01 19:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0018_rename_blog_badge_post_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='badge',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=200, null=True, unique=True),
        ),
    ]