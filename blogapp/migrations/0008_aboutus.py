# Generated by Django 4.0.1 on 2022-01-13 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_remove_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=500)),
                ('about_us', models.TextField(max_length=10000)),
            ],
        ),
    ]