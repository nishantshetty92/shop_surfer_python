# Generated by Django 4.2.2 on 2023-06-28 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_orderitem_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=150)),
                ('mobile_number', models.CharField(max_length=10)),
                ('pin_code', models.CharField(max_length=10)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(blank=True, max_length=150)),
                ('state', models.CharField(blank=True, max_length=150)),
                ('is_default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.product'),
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
    ]
