# Generated by Django 3.2.4 on 2022-04-24 14:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_aboutus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'Comment'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Post'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='about_us',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
