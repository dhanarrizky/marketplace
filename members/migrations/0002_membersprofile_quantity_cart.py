# Generated by Django 4.2 on 2023-06-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersprofile',
            name='quantity_cart',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
