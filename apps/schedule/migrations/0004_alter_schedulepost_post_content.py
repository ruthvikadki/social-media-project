# Generated by Django 4.2.10 on 2024-02-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0003_alter_schedulepost_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedulepost",
            name="post_content",
            field=models.TextField(max_length=20),
        ),
    ]
