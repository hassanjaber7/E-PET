# Generated by Django 4.2.6 on 2023-10-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_alter_product_image_alter_product_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]