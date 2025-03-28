# Generated by Django 4.2.7 on 2024-01-05 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0038_alter_reviewfood_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.FloatField(default=0.0)),
                ("amount", models.IntegerField(default=0)),
                ("date", models.DateField(blank=True, null=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[
                            ("expenses", "expenses"),
                            ("income", "income"),
                            ("leftover", "Leftover"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
