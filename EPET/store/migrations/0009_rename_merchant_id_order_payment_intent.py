# Generated by Django 4.2.6 on 2023-10-17 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_order_total_cost_order_paid_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merchant_id',
            new_name='payment_intent',
        ),
    ]
