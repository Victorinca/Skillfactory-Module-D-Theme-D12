# Generated by Django 4.2.6 on 2023-10-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_subscription_subscriptioncreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscriptionCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
