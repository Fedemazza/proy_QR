# Generated by Django 4.2.1 on 2023-06-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("explorador", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="qr",
            name="id",
        ),
        migrations.AlterField(
            model_name="qr",
            name="serialnum",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]