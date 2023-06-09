# Generated by Django 4.1.7 on 2023-03-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("title", models.CharField(max_length=150, unique=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=150,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
    ]
