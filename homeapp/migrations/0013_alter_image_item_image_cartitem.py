# Generated by Django 4.2.4 on 2023-09-06 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0012_rename_item_id_image_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='item_image',
            field=models.ImageField(null=True, upload_to='itemssingle'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('user_session', models.CharField(max_length=32)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.item')),
            ],
        ),
    ]
