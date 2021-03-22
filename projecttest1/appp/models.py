from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
class StudentDetails:
    email: str
    password: str
    StudentName: str
    studentId: int
    mobileno: int
    adress: str
    country: str
    SSC_cgpa: float
    inter_marks: int
    UG_Current_cgpa: float
    total_backlogs: int
    active_backlogs: int
    projects: str
    skills: str



class Material(models.Model):
    FileName=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='materials/pdfs/')

    def __str__(self):
        return self.FileName


class student(models.Model):
    branches=(('1','ECE'),('2','CES'),('3','EEE'),('4','ME'))
    username =  models.OneToOneField(User, on_delete=models.CASCADE)
    Student_image = models.FileField(upload_to='StudentPics/',default="https://th.bing.com/th/id/OIP.ARJrx9vRGJcvJDizj8UgPgHaGR?w=259&h=220&c=7&o=5&pid=1.7")
    student_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    Address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    tenth = models.CharField(max_length=255)
    twelve = models.CharField(max_length=255) 
    cgpa = models.FloatField(max_length=3)
    no_backlog = models.IntegerField()
    c_backlog = models.IntegerField() 
    branch=models.CharField(choices=branches,blank=True,max_length=3)
    Placement_status= models.BooleanField(default=False)
    
    def __str__(self):
        return self.student_name

class Company(models.Model):
    Company_name = models.CharField(max_length=255)
    About_company = models.TextField()
    Company_link = models.URLField(max_length=255)
    Jobrole = models.CharField(max_length=255)
    Job_responsilities = models.TextField()
    Job_Salary = models.FloatField(max_length=5)
    Eligibility_cgpa = models.FloatField(max_length=3)
    Eligibility_branches = models.TextField()
    Eligible_Passedout_Batchs = models.CharField(max_length=255)
    Eligibility_education_gap = models.IntegerField()
    application_start_date =models.DateField(null=True)
    application_end_date = models.DateField(null=True)
    not_eligible = models.IntegerField(default=0)
    not_attended = models.IntegerField(default=0)
    written_selects = models.IntegerField(default=0)
    tr_selects = models.IntegerField(default=0)
    final_selects = models.IntegerField(default=0)
    
    def __str__(self):
        return self.Company_name


class Post(models.Model):
    Post_Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Post_Title = models.CharField(max_length=255, blank=True)
    Post_Subject = models.CharField(max_length=255, blank=True)
    Post_body = models.TextField(blank=True)
    Post_CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Post_Title   




        

