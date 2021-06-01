from django.db import models

# Create your models here.
class register1(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=1)
    username=models.CharField(max_length=20,unique=True)
    countrycode=models.CharField(max_length=10,choices=(("+91","+91"),("+123","+123")),default="select countrycode")
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=20,default=12345678)
class post(models.Model):
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=200)
    username=models.ForeignKey(register1,on_delete=models.CASCADE,null=True,default=1)






