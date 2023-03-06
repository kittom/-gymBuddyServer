# Generated by Django 4.1.7 on 2023-02-24 20:21

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('gymbuddyapi', '0002_account_unique_username'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='account',
            constraint=models.UniqueConstraint(models.OrderBy(django.db.models.functions.text.Lower('email'), descending=True), name='unique_email'),
        ),
    ]
