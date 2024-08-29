from django.db import models

# Create your models here.

class Login(models.Model):
    Username=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)
    Emailid=models.EmailField()
    
