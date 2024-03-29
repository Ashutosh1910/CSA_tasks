# Generated by Django 4.2.9 on 2024-01-28 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_items', models.PositiveIntegerField(default=0)),
                ('total_cost', models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('bits_id', models.CharField(max_length=15)),
                ('hostel', models.CharField(choices=[('SR', 'SR'), ('GANDHI', 'GANDHI'), ('KRISHNA', 'KRISHNA'), ('RAM', 'RAM'), ('BUDH', 'BUDH'), ('SHANKAR', 'SHANKAR'), ('VYAS', 'VYAS'), ('RANAPRATAP', 'RANAPRATAP'), ('VK', 'VK'), ('ASHOK', 'ASHOK'), ('MEERA', 'MEERA'), ('BHAGIRATH', 'BHAGIRATH')], default='SR', max_length=10)),
                ('room_no', models.PositiveIntegerField(default=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Basket_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_quantity', models.PositiveIntegerField(default=1)),
                ('item_cost', models.PositiveBigIntegerField(default=0)),
                ('item_name', models.CharField(max_length=25)),
                ('item_description', models.TextField()),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='item_images/')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.basket')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_interface.user_profile'),
        ),
    ]
