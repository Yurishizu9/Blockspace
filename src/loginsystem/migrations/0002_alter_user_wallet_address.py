# Generated by Django 4.0.2 on 2022-05-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=42, null=True, unique=True),
        ),
    ]
