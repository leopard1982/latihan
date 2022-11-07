# Generated by Django 4.1.3 on 2022-11-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="daftarnama",
            name="kelamin",
            field=models.CharField(
                choices=[("L", "Laki-laki"), ("P", "Perempuan")],
                default="L",
                max_length=1,
                verbose_name="Jenis Kelamin",
            ),
        ),
    ]