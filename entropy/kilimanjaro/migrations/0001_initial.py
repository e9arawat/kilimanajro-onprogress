# Generated by Django 4.2.9 on 2024-03-13 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("slug", models.CharField(max_length=50)),
                ("joined_at", models.DateField()),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Trainee", "Trainee"),
                            ("Developer", "Developer"),
                            ("HR", "HR"),
                            ("Analyst", "Analyst"),
                        ],
                        default="Trainee",
                        max_length=50,
                    ),
                ),
                ("earned_leaves", models.IntegerField(default=24)),
                ("is_authorized", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Absent", "Absent"),
                            ("Late", "Late"),
                            ("Sick", "Sick"),
                            ("Travel", "Travel"),
                            ("Vacation", "Vacation"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendance",
                        to="kilimanjaro.employee",
                    ),
                ),
            ],
        ),
    ]