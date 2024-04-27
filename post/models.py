from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.TextField()
    size = models.IntegerField()
    image = models.ImageField(upload_to='previev/', blank=True, null=True)

    def __str__(self):
        return self.name