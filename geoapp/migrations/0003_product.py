# Generated by Django 4.2.8 on 2024-01-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0002_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(max_length=20)),
                ('productName', models.CharField(max_length=50)),
                ('productPrice', models.FloatField()),
            ],
        ),
    ]
