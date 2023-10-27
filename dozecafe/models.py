from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Coffee(models.Model):
    name= models.CharField(max_length=40)
    description= models.CharField(max_length=100)
    img = models.ImageField(upload_to='product_img')
    price= models.FloatField()
    
    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.ForeignKey(User,  related_name='cust_name', on_delete=models.CASCADE)
    address= models.CharField(max_length=100)
    product = models.ForeignKey(Coffee,  related_name='product', on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1) 
    total_cost = models.FloatField() 
    
    
    # Get price
    def get_price(self):
        pro_id = Coffee.objects.get(id=self.product.id)
        return pro_id.price

    # Calculate total cost
    def cal_total(self):
        pro_id = Coffee.objects.get(id=self.product.id)
        return pro_id.price * self.quantity
    
    def save(self, *args, **kwargs):
        self.price = self.get_price()
        self.total_cost = self.cal_total()

        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name}-{self.id}"

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=12)
    message=models.TextField()

    def __str__(self):
        return self.name
    
# for blog
class Blog(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField(default=datetime.today())
    img=models.ImageField()
    description=models.TextField()

    def __str__(self):
        return self.name