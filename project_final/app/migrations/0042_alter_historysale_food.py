# Generated by Django 4.2.7 on 2024-01-31 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0041_alter_food_options_fooditem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historysale",
            name="food",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.fooditem",
            ),
        ),
    ]
