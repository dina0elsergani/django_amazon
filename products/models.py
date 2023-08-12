from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    image = models.ImageField(upload_to='categories/')
    def get_show_url(self):
        return reverse('category_detail', args=[self.id])
    def get_edit_url(self):
        return reverse('category_edit', args=[self.id])
    def get_delete_url(self):
        return reverse('category_delete', args=[self.id])
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    instock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_show_url(self):
        return reverse('product_show', args=[self.id])

    def get_edit_url(self):
        return reverse('product_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('product_delete', args=[self.id])

