from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATOGORY = (("sciencebook", "sciencebook"), ("mathbook", "mathbook"), ("english", "english"))
    name = models.CharField(max_length=20,null=True)
    catogory = models.CharField(max_length=20, choices=CATOGORY,null= True)
    quantity = models.PositiveIntegerField(null=True)




    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order_quantity=models.PositiveIntegerField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}'
