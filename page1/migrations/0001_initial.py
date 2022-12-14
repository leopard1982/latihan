# Generated by Django 4.1.2 on 2022-11-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Daftarnama",
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
                ("nama", models.CharField(max_length=100, verbose_name="Nama Anda")),
                (
                    "alamat",
                    models.CharField(max_length=100, verbose_name="Alamat Anda"),
                ),
            ],
            options={
                "ordering": ["nama"],
                "unique_together": {("nama", "alamat")},
            },
        ),
    ]
