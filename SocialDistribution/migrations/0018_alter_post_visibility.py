# Generated by Django 5.0.1 on 2024-02-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialDistribution', '0017_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('FRIENDS', 'Friends-Only'), ('PRIVATE', 'Private')], default='PUBLIC', max_length=10),
        ),
    ]