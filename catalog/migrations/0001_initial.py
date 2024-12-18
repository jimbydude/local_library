# Generated by Django 5.1.4 on 2024-12-17 05:19

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                    "name",
                    models.CharField(
                        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)",
                        max_length=200,
                        unique=True,
                    ),
                ),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(
                        django.db.models.functions.text.Lower("name"),
                        name="genre_name_case_insensitive_unique",
                        violation_error_message="Genre already exists (case insensitive match)",
                    )
                ],
            },
        ),
    ]
