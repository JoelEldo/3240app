# Generated by Django 4.2.10 on 2024-04-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a10app', '0013_report_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='flagged',
            field=models.BooleanField(default=False),
        ),
    ]