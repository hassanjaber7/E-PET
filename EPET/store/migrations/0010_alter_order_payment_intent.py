# Generated by Django 4.2.6 on 2023-10-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_merchant_id_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(max_length=255, null=True),
        ),
    ]