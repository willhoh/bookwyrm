# Generated by Django 3.2.15 on 2022-09-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0157_auto_20220909_2338"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="htop_count",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="otp_secret",
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="two_factor_auth",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
