# Generated by Django 5.0.6 on 2024-05-18 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend_server", "0039_workouttype_processed"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkoutAnalysis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avg_speed",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "max_speed",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "total_distance",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                ("avg_heart_rate", models.IntegerField(blank=True, null=True)),
                ("workout_duration", models.DurationField(blank=True, null=True)),
                (
                    "avg_temperature",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "session_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="session_id_workoutanalysis",
                        to="backend_server.workouttype",
                    ),
                ),
            ],
        ),
    ]
