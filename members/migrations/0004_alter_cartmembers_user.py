# Generated by Django 4.2 on 2023-06-03 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0003_remove_membersprofile_quantity_cart_cartmembers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmembers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]