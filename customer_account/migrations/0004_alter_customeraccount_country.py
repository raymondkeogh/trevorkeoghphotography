# Generated by Django 3.2.6 on 2021-09-14 19:02

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):
    """Change tp customer account countryfield"""
    dependencies = [
        ('customer_account', '0003_remove_customeraccount_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='country',
            field=django_countries.fields.CountryField(
                blank=True,
                max_length=2,
                null=True),
        ),
    ]