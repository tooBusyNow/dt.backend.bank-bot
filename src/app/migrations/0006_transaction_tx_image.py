# Generated by Django 4.2.1 on 2023-05-17 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_remove_remoteimage_remote_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="tx_image",
            field=models.OneToOneField(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="transaction",
                to="app.remoteimage",
            ),
        ),
    ]
