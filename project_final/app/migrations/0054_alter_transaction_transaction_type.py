# Generated by Django 4.2.7 on 2024-02-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0053_alter_transaction_transaction_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[
                    ("expenses", "expenses"),
                    ("income", "income"),
                    ("leftover", "Leftover"),
                ],
                max_length=10,
            ),
        ),
    ]
