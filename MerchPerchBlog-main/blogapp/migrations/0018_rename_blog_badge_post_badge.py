# Generated by Django 3.2.4 on 2022-05-01 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_alter_post_blog_badge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog_badge',
            new_name='badge',
        ),
    ]
