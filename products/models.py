from django.db import models


PRODUCT_TYPE_CHOICES = (
    ("Mobile", "Mobile"),
    ("Laptop", "Laptop"),
)


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    processor = models.CharField(max_length=500)
    ram = models.CharField(max_length=500)
    screen_size = models.CharField(max_length=100, null=True, blank=True) # for products with type Mobile
    color = models.CharField(max_length=100, null=True, blank=True) # for products with type Mobile
    hd_capacity = models.CharField(max_length=100, null=True, blank=True) # for products with type Laptop

    def __str__(self):
        return f"{self.name}"
        