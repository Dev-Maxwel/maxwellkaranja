# Generated by Django 4.2.6 on 2024-01-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="emailingInfo",
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "phone",
                    models.PositiveIntegerField(blank=True, max_length=50, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=70, null=True)),
                ("message", models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]