# Generated by Django 4.2.9 on 2024-01-29 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller_interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_order',
            name='order_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller_interface.restraunt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restraunt',
            name='of_seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seller_interface.seller_profile'),
        ),
    ]