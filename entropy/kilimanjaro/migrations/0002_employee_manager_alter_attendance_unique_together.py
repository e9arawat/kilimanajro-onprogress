# Generated by Django 4.2.9 on 2024-03-13 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("kilimanjaro", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee",
                to="kilimanjaro.employee",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="attendance",
            unique_together={("employee", "date")},
        ),
    ]
