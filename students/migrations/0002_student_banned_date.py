# Generated by Django 4.1.7 on 2023-03-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="banned_date",
            field=models.DateField(null=True),
        ),
    ]
