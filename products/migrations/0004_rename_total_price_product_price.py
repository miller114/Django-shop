# Generated by Django 4.0.5 on 2022-06-10 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_is_active_product_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='total_price',
            new_name='price',
        ),
    ]
