# Generated by Django 5.0.6 on 2024-05-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_logger', '0003_location_bogon_location_success_alter_log_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
