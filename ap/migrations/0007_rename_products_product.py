# Generated by Django 4.2.3 on 2023-08-08 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0006_products_alter_customer_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
