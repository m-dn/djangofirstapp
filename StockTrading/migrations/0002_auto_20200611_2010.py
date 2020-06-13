# Generated by Django 2.2.13 on 2020-06-11 18:10

import StockTrading.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockTrading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=8, validators=[StockTrading.models.validator]),
        ),
    ]