# Generated by Django 4.2.1 on 2023-05-17 00:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RemoteImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("content", models.FileField(upload_to="")),
            ],
        ),
    ]