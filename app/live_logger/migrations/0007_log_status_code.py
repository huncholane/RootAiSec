# Generated by Django 5.0.6 on 2024-05-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_logger', '0006_rename_loc_log_location_remove_log_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='status_code',
            field=models.IntegerField(null=True),
        ),
    ]