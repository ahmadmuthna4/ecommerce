# Generated by Django 4.0.4 on 2022-05-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderdetails_options_order2_details_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expire',
            field=models.CharField(max_length=150),
        ),
    ]
