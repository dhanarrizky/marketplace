from django.contrib import admin
from .models import membersProfile, cartMembers
from django.contrib.auth.models import User


# Register your models here.

admin.site.register(membersProfile)
admin.site.register(cartMembers)
