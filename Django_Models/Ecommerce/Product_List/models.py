from django.db import models


# Create your models here.

class Product(models.Model):
    PRODUCT_TYPES = [
        ('TECH',"Laptop"),
        ('EDU', 'Book'),
        ('SPT', 'Stamp'),
        ('FMCG', 'Kurkure'),
        ('SD', 'Cocacola'),
    ]

    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=3 )
    prodct_type = models.CharField(max_length=4,choices=PRODUCT_TYPES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    #image = models.ImageField(upload_to='images/', default='images/default.jpg')


    def __str__(self):
        return self.product_name