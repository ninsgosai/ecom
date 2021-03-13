from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200,verbose_name="Product Name")
    image = models.ImageField(verbose_name="Product Image" ,upload_to="products")
    price = models.CharField(max_length=200,verbose_name="Product Price")
    SKU = models.CharField(max_length=200,verbose_name="Product Units")
    description = models.CharField(max_length=200,verbose_name="Product Description")