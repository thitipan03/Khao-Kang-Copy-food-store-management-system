# Generated by Django 4.2.7 on 2024-04-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0094_alter_member_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="line_id",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
