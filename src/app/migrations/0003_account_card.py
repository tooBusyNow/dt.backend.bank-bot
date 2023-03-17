# Generated by Django 4.2b1 on 2023-03-09 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_user_alter_adminuser_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("uniq_id", models.CharField(max_length=20, primary_key=True, serialize=False)),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("USD", "United States dollar"),
                            ("EUR", "Euro"),
                            ("GBP", "British pound"),
                            ("TRY", "Turkish lira"),
                            ("RUB", "Russian ruble"),
                        ],
                        max_length=3,
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=19)),
                ("party", models.CharField(choices=[("PER", "Person"), ("ENT", "Entity")], max_length=3)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.user")),
            ],
            options={
                "verbose_name": "Account",
                "db_table": "payment_accounts",
            },
        ),
        migrations.CreateModel(
            name="Card",
            fields=[
                ("uniq_id", models.CharField(max_length=20, primary_key=True, serialize=False)),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("USD", "United States dollar"),
                            ("EUR", "Euro"),
                            ("GBP", "British pound"),
                            ("TRY", "Turkish lira"),
                            ("RUB", "Russian ruble"),
                        ],
                        max_length=3,
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=19)),
                ("expiration", models.DateField()),
                (
                    "corresponding_account",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.account"),
                ),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.user")),
            ],
            options={
                "verbose_name": "Card",
                "db_table": "payment_cards",
            },
        ),
    ]
