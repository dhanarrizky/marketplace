# Generated by Django 4.2 on 2023-06-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestWebsite', '0002_alter_goods_for_sale_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_for_sale',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
