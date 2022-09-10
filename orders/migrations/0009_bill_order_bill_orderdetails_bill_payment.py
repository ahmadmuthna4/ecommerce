# Generated by Django 4.0.4 on 2022-05-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_bill_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order2'),
        ),
        migrations.AddField(
            model_name='bill',
            name='orderdetails',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderdetails'),
        ),
        migrations.AddField(
            model_name='bill',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.payment'),
        ),
    ]
