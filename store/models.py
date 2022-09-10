from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    img=models.ImageField(upload_to='img',blank=True,null=True)
    category=models.CharField(max_length=30)
    descriotion=models.TextField()


    def __str__(self):
        return self.name
        
    class Meta:
        ordering=['-id']     


class Order(models.Model):
    name=models.CharField(max_length=200)
    number_Phone=models.CharField(max_length=200)
    addres=models.CharField(max_length=200)
    number_order=models.CharField(max_length=200)
    count_order=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    like_product=models.ManyToManyField(Product)
    adress=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    # img=models.ImageField(upload_to='img2',blank=True,null=True)


    def __str__(self):
        return self.user.username   

    class Meta:
        ordering=['-id']   