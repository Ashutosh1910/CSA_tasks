# Generated by Django 4.2.9 on 2024-01-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_interface', '0002_pending_order_order_to_alter_restraunt_of_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_order_item',
            name='item_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
