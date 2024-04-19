from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title
    

class Post(models.Model):
    title=models.CharField(max_length=255)
    sub_title=models.CharField(max_length=255)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="static",default='image')
    def __str__(self):
        return self.title
    
class ProductCategory(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Product(models.Model):
    productname=models.CharField(max_length=255)
    prdctprc=models.BigIntegerField()
    desc=models.TextField()
    desc2=models.TextField()
    img=models.ImageField( upload_to="static",default='image')
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    
class Profile(models.Model):
        user=models.OneToOneField(User, on_delete=models.CASCADE)
        phonenumber=models.BigIntegerField(default=0)
        place=models.TextField() 
        image=models.ImageField( upload_to="UserImage")

class Feedback(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField( max_length=254)   
     message=models.TextField(max_length=250)

class BookaTable(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=50,default="unknown")
    email=models.EmailField(max_length=254,default=0)
    phonenumber=models.BigIntegerField(default=0)
    noOfperson=models.IntegerField(default=0)
    date=models.DateField( auto_now=False, auto_now_add=False)

class Shipping(models.Model):
    full_name=models.CharField( max_length=50)
    address=models.CharField(max_length=250)
    phone=models.BigIntegerField(max_length=50)
    city=models.CharField(max_length=50)
    pin_code=models.BigIntegerField(max_length=50)
    created_at=models.DateField(auto_now_add=True)
    
class CartItem(models.Model):
    order=models.ForeignKey(Shipping, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    # total_price=models.DecimalField(max_digits=10, decimal_places=2)
    # def __str__(self):
    #     return self.name

class UserOrder(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal=models.DecimalField(max_digits=10, decimal_places=2)
    shipping_details=models.ForeignKey(Shipping,on_delete=models.CASCADE)
