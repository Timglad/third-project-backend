from django.db import models

# Create your models here.


class Product(models.Model):
    class CartStatus(models.TextChoices):
        ACTIVE = 'A', 'In Cart'
        NOTACTIVE = 'N', 'Not in Cart'

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    status = models.CharField(max_length=1, choices=CartStatus.choices, default=CartStatus.NOTACTIVE)




# class Order
# DateField
# OrderID


# class OrderItem(models.Model)
#     user
#     OrderID = 
#     product = models.ForeignKey(Product)
#     quantiy = models.IntegerField()
# user order productid quantity
# 1     1       2         2
# 1  3   1
# 1  4   1
