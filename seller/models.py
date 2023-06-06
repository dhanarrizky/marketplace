from django.db import models
from django.contrib.auth.models import User
from members.models import cartMembers

# Create your models here.
class sellerProfile(models.Model):
    user = models.OneToOneField(User, related_name = "sellers", on_delete=models.CASCADE)
    companyname = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    addressseller = models.TextField(blank=True, null=True)
    picture_company = models.ImageField(upload_to="companyPic/",blank=True, null=True)
    
    def __str__(self):
        return str(self.companyname)
    
class reqClient(models.Model):
    client = models.ForeignKey(cartMembers, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return str(self.client)
    