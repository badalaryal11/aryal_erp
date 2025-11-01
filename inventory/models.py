from django.db import models

# A model to group similar products
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories" # Fixes display name in admin

    def __str__(self):
        return self.name

# The core model for the items sold by Aryal Agro Enterprises
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, # If a category is deleted, products remain but category field is set to NULL
        null=True
    )
    sku = models.CharField(max_length=50, unique=True, help_text="Stock Keeping Unit / Product Code")
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"