# Generated by Django 3.2.3 on 2021-08-16 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_remove_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='code',
            new_name='price',
        ),
    ]