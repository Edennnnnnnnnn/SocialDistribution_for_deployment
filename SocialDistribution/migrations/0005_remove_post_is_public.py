# Generated by Django 5.0.2 on 2024-02-19 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialDistribution', '0004_post_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_public',
        ),
    ]
