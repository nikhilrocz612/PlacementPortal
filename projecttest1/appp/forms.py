from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import student,Material,Company,Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('FileName','pdf')

class Companyforms(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('Post_Author','Post_Title','Post_Subject','Post_body')
        
         
class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('username','student_name','Student_image','phone','Address','country','tenth','twelve','cgpa','branch','no_backlog','c_backlog','Placement_status')
