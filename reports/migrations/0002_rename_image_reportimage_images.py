# Generated by Django 4.1.7 on 2023-03-17 05:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reportimage",
            old_name="image",
            new_name="images",
        ),
    ]
