# Generated by Django 5.2.3 on 2025-07-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0005_society_cancel_token_society_cancel_token_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='society',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
