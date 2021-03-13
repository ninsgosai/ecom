from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200,verbose_name="User Name")
    email = models.CharField(max_length=200,verbose_name="Email")
    password = models.CharField(max_length=200,verbose_name="Password")
    confirm_password = models.CharField(max_length=200,verbose_name="Confirm Password")
    image = models.ImageField(verbose_name="Product Image" ,upload_to="profile")