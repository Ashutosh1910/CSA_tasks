# Generated by Django 4.2.9 on 2024-01-28 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', models.PositiveBigIntegerField(default=0)),
                ('item_name', models.CharField(max_length=25)),
                ('item_description', models.TextField()),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='item_images/')),
                ('available', models.BooleanField(default=True)),
                ('item_rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pending_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.PositiveBigIntegerField(default=0)),
                ('no_of_items', models.PositiveIntegerField(default=0)),
                ('of_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.user_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Restraunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restraunt_name', models.CharField(max_length=15)),
                ('restraunt_rating_value', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Seller_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_phone_no', models.PositiveBigIntegerField(default=9999999999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restraunt_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField(default=5)),
                ('rated_restraunt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller_interface.restraunt')),
                ('rating_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='restraunt',
            name='of_seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller_interface.seller_profile'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField(default=5)),
                ('rated_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller_interface.item')),
                ('rating_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pending_Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', models.PositiveBigIntegerField(default=0)),
                ('item_name', models.CharField(max_length=25)),
                ('of_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller_interface.pending_order')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='of_restraunt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller_interface.restraunt'),
        ),
    ]
