# Generated by Django 4.0.4 on 2022-06-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total_prices',
            field=models.FloatField(default=0),
        ),
    ]
