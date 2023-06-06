from django.contrib import admin
from .models import goods_for_sale, category
# Register your models here.

admin.site.register(goods_for_sale)
admin.site.register(category)