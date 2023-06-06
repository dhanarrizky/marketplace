from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class goods_for_sale(models.Model):
    user = models.ForeignKey(User, related_name="goods", on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(category, related_name="goods", on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank= True, null=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(blank=True)
    stock = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    
    
    