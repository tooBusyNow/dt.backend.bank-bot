# Generated by Django 4.2 on 2023-04-13 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_account_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("tx_id", models.AutoField(primary_key=True, serialize=False)),
                ("tx_timestamp", models.DateTimeField(auto_now_add=True)),
                ("tx_value", models.DecimalField(decimal_places=2, max_digits=19)),
                (
                    "tx_recip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="recip", to="app.account"
                    ),
                ),
                (
                    "tx_sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="sender", to="app.account"
                    ),
                ),
            ],
            options={
                "verbose_name": "Transaction",
                "db_table": "payment_transactions",
                "ordering": ["tx_timestamp"],
            },
        ),
    ]
