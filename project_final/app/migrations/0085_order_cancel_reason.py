# Generated by Django 4.2.7 on 2024-03-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0084_remove_order_cancel_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="cancel_reason",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
