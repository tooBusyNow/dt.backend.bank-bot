# Generated by Django 4.2b1 on 2023-03-23 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_card_currency_remove_card_owner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="owner",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="app.user"),
        ),
    ]
