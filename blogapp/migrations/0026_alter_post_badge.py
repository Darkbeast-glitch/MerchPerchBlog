# Generated by Django 3.2.4 on 2022-05-01 20:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0025_post_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='badge',
            field=models.CharField(default=uuid.uuid1, max_length=200, unique=True),
        ),
    ]
