from django.db import models
from django import forms
from passwords.fields import PasswordField

# Create your models here.


class StudentAccount(models.Model):
    StudentID=models.BigIntegerField()
    StudentPassword=models.CharField(max_length=50,default='klef123')
    Student_name = models.CharField(max_length=255)
    Student_email = models.EmailField(max_length=255,null=True,default=None)
    Gender = models.CharField(max_length=1,default=" ")
    Branch=models.CharField(max_length=3)
    PhoneNo = models.BigIntegerField()
    Address = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Tenth = models.CharField(max_length=255)
    Twelvth = models.CharField(max_length=255) 
    Present_Cgpa = models.FloatField(max_length=3)
    Total_backlogs = models.IntegerField()
    Active_backlogs = models.IntegerField() 
    Placement_status= models.BooleanField(default=False)
    TCS=models.CharField(max_length=10)
    Cognizant=models.CharField(max_length=10)
    Capgemini=models.CharField(max_length=10)
    MindTree=models.CharField(max_length=10)
    Infosys=models.CharField(max_length=10)
    Wipro=models.CharField(max_length=10)
    Deloitte=models.CharField(max_length=10)
    HCL=models.CharField(max_length=10)
    Accenture=models.CharField(max_length=10)
    IBM=models.CharField(max_length=10)
    
    def __str__(self):
        return self.Student_name