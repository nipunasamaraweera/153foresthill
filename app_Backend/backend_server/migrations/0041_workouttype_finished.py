# Generated by Django 5.0.6 on 2024-05-19 04:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend_server", "0040_workoutanalysis"),
    ]

    operations = [
        migrations.AddField(
            model_name="workouttype",
            name="finished",
            field=models.BooleanField(default=False),
        ),
    ]