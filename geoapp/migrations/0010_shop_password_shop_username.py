# Generated by Django 4.2.8 on 2024-01-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0009_alter_product_productid'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='password',
            field=models.CharField(default='password', max_length=15),
        ),
        migrations.AddField(
            model_name='shop',
            name='username',
            field=models.CharField(default='User', max_length=10),
        ),
    ]
