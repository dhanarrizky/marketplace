# Generated by Django 4.2 on 2023-06-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestWebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_for_sale',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='goods_for_sale',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goods_for_sale',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
