# Generated by Django 4.2.7 on 2024-02-29 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0068_rename_price_orderitemtype1_total_price_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitemtype2",
            old_name="total_price",
            new_name="price",
        ),
    ]
