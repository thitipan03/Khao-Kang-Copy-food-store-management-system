# Generated by Django 4.2.7 on 2023-12-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0034_delete_place"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member",
            old_name="name",
            new_name="first_name",
        ),
        migrations.RemoveField(
            model_name="member",
            name="user_name",
        ),
        migrations.AddField(
            model_name="member",
            name="last_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
