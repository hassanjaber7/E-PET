# Generated by Django 4.2.6 on 2023-10-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'Waiting approval'), ('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
    ]