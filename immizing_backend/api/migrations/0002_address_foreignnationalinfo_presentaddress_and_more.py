# Generated by Django 4.1.6 on 2023-02-08 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("api", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("Street", models.TextField(max_length=500)),
                ("city", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("zip_code", models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name="foreignnationalinfo",
            name="presentAddress",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="api.address"
            ),
        ),
        migrations.AddField(
            model_name="foreignnationalinfo",
            name="previousAddresses",
            field=models.ManyToManyField(
                related_name="previousAddress", to="api.address"
            ),
        ),
    ]
