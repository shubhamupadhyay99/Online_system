from django.db import models
from django.urls import reverse


class Product(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

class PurchaseOrder(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    buying_date = models.DateTimeField(auto_now_add=True)
