# Generated by Django 4.2.2 on 2023-06-22 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cartitem_is_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 6, 22, 13, 32, 49, 309702)),
            preserve_default=False,
        ),
    ]