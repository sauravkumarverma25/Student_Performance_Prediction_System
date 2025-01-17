# Generated by Django 5.0.1 on 2024-02-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "student_analysis",
            "0002_remove_studymaterial_file_studymaterial_student_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentPerformanceData",
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
                ("seat_no", models.CharField(max_length=100)),
                ("student_name", models.CharField(max_length=255)),
                ("performance_level", models.CharField(max_length=50)),
                ("subject_name", models.CharField(max_length=255)),
                ("score", models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name="StudentPerformance",
        ),
    ]
