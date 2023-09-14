# Generated by Django 4.2.4 on 2023-08-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_rename_shop_shopgrid'),
    ]

    operations = [
        migrations.CreateModel(
            name='shops1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_imag5', models.ImageField(null=True, upload_to='images')),
                ('product_name5', models.CharField(max_length=50)),
                ('product_price5', models.IntegerField(null=True)),
                ('product_rate5', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shopsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_imag6', models.ImageField(null=True, upload_to='images')),
                ('product_name6', models.CharField(max_length=50)),
                ('product_price6', models.IntegerField(null=True)),
                ('product_rate6', models.IntegerField(null=True)),
            ],
        ),
    ]