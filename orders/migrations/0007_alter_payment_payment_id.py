# Generated by Django 4.0.1 on 2022-02-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
