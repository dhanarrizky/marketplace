from django.db import models
from django.contrib.auth.models import User
from guestWebsite.models import goods_for_sale
from django.template.defaultfilters import slugify


# Create your models here.

    
    
class membersProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='profilePic/')
    mypay = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    #complete profile
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    Country = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    mobile_no = models.IntegerField(blank=True, default=0)
    zip_code = models.IntegerField(blank=True, default=0)
    cart = models.ManyToManyField(goods_for_sale,related_name='memberscart', blank= True)
    
    def __str__(self):
        return str(self.username)
    
    def cartCount(self):
        return self.cart.count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)
    
    
class cartMembers(models.Model):
    user = models.ForeignKey(membersProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(goods_for_sale, on_delete=models.CASCADE,default=1)
    quantity_cart = models.FloatField(default=1,blank=True)
    Total_per_product = models.FloatField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.product:
            self.Total_per_product = self.product.price * self.quantity_cart
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.user)