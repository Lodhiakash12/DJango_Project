from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.PositiveBigIntegerField()
    profile_picture=models.ImageField(upload_to="profile_picture/")
    address=models.TextField()
    email=models.EmailField()
    password=models.CharField(max_length=100)
     

    def __str__(self):
        return self.fname+""+self.lname