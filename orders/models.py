from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class Order2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    details=models.ManyToManyField(Product, through='OrderDetails')
    is_fished=models.BooleanField()


    def __str__(self):
        return 'User:'+self.user.username +', order id: ' +str(self.id)

class OrderDetails(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order2,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    quantity=models.IntegerField()


    def __str__(self):
        return 'User:'+ self.order.user.username +' ,product: ' + self.product.name +', Order id :' +str(self.order.id)


    class Meta:
        ordering=['-id']     


class Payment(models.Model):
    order=models.ForeignKey(Order2,on_delete=models.CASCADE)
    adress=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
   

    def __str__(self):
        return str(self.id)
    




