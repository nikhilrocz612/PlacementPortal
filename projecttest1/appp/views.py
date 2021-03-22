import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import Group, User
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
import io,csv
from io import TextIOWrapper
from django.views import View

from .decorators import allowed_users, unauthenticated_user
from .forms import *
from .models import *
from StudentAccount.models import StudentAccount

# Create your views here.

def home(request):
    count = User.objects.count()
    posts=Post.objects.all()
    return render(request, 'home.html',{'posts':posts})


@unauthenticated_user
def signup(request):    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='students')
            user.groups.add(group)
            return redirect('home')    
    else:        
        form = CreateUserForm()
    return render(request,'registration/signup.html' , {
            'form': form
        })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['SuperUsers'])
def tpo_signup(request):    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            tpo=User.objects.get(username=user.username)
            tpo.is_staff=True
            tpo.save()
            group = Group.objects.get(name='TPO')
            user.groups.add(group)
            return redirect('home')    
    else:        
        form = CreateUserForm()
    return render(request, 'registration/tpo_signup.html' , {
            'form': form
        })


@unauthenticated_user
def loginPage(request):   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,username)
            return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect') 
    context = {}           
    return render(request, 'registration/login.html',context)

@login_required(login_url='accounts/login')
def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','SuperUsers'])
def companySignup(request):
    if request.method == 'POST':
        form = Companyforms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' New Company has been updated  successfully...!')
            return redirect('CompanyList')
    else:        
        form = Companyforms()
    return render(request, 'registration/CopmanySignupform.html' , {
        'form': form
    })  



@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','SuperUsers'])
def AddPost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' New post has been updated  successfully...!')
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'Posts.html', {'form': form})  


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','SuperUsers'])
def StudentFilter(request):
    stu = StudentAccount.objects.all()
    return render(request, 'StudentList.html',{
        'stu' : stu
    })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','students','SuperUsers'])
def CompanyYetToCome(request):
    liste=Company.objects.filter(application_start_date__gt = datetime.date.today()).order_by('application_start_date')
    return render(request, 'CompanyList.html', {
        'liste' : liste
    })

@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','students','SuperUsers'])
def CompaniesVisited(request):
    liste=Company.objects.filter(application_end_date__lt = datetime.date.today()).order_by('application_end_date')
    return render(request, 'CompanyList.html', {
        'liste' : liste
    })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','students','SuperUsers'])
def CompanyData(request,name):
    companyd=Company.objects.get(Company_name=name)
    return render(request, 'CompanyData.html', {
        'companyd' : companyd
    })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','SuperUsers'])
def StudentsList(request, name):
    Wanted=Company.objects.get(Company_name=name)
    tcgpa=Wanted.Eligibility_cgpa
    stu={}
    stu=StudentAccount.objects.filter(Present_Cgpa__gte = tcgpa)
    return render(request, 'StudentList.html',{
        'stu' : stu
    })
 

@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','students','SuperUsers'])
def materials_list(request):
    materials = Material.objects.all()
    return render(request, 'materials_list.html', {
        'materials' : materials
    })

@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','students','SuperUsers'])
def CompanyList(request):
    liste = Company.objects.order_by('Company_name')
    return render(request, 'CompanyList.html', {
        'liste' : liste
    })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','SuperUsers'])
def upload_materials(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ' New material has been updated  successfully...!')
            return redirect('materials')
    else:
        form = MaterialForm()        
    return render(request, 'upload_materials.html', {
        'form': form
        })


@login_required(login_url='accounts/login')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('password_change')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['students'])
def EligibleCompanies(request,id):
    temp=student.objects.get(username_id = id)
    tcgpa=temp.cgpa
    backlogs=temp.c_backlog
    liste=Company.objects.filter(Eligibility_cgpa__lte = tcgpa,)
    return render(request, 'Eligiblecompanies.html', {
        'liste' : liste
    })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['students'])
def Studentsignup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            usertemp = request.user
            instance.Student_name=usertemp.username
            instance.save()
            return redirect('home')
    else:        
        form = StudentForm()
    return render(request, 'registration/Studentsignup.html' , {
        'form': form
    })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','SuperUsers'])
def StudentProfileDisplay(request,stuid):
    sp={}
    sp = StudentAccount.objects.get( id = stuid )
    return render(request, 'profile.html', {'sp': sp })


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['students'])
def Update_Sprofile(request, userid): 
    instance = student()
    instance = get_object_or_404(student, username_id=userid)
    form = StudentForm(request.POST, instance=instance)
    if request.POST and form.is_valid():
        form.save()
    return render(request, 'registration/Studentsignup.html', {'form': form})


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['students'])
def Update_Sprofile(request,userid):

    stu = student.objects.get(username_id=userid)
    form = StudentForm(instance=stu)

    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('home')        
    return render(request, 'registration/user_profile.html', {
        'form': form
        })



def mamul(request):
    return render(request, 'mamul.html')

def LoginPage(request):
    return render(request, 'LoginPage.html')

def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='accounts/login')
def profile(request):
    de=StudentDetails()
    de.StudentName="acharya"
    de.studentId= 1245
    return render(request , 'profile.html')


@login_required(login_url='accounts/login')
def upload(request):
    context = {}
    if request.method=='POST':
        uploaded_file=request.FILES['myfile']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        url=fs.url(name)
        context['url'] = fs.url(name)
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'upload.html')  


@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['TPO','SuperUsers'])
def delete_materials(request,id):
    if request.method == 'POST':
        material = Material.objects.get(id=id)
        material.delete()
        messages.success(request, '  Material has been deleted successfully...!')
    return redirect('materials')


class cuv(View):
    def get(self, request):
        template_name = 'employee/importemployee.html'
        return render(request, template_name)
    def post(self,request):

        user = request.user  # get the current login user details
        Company.objects.all().delete()
        paramFile = TextIOWrapper(request.FILES['employeefile'].file,encoding="utf-8-sig",errors='ignore')
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
            Company(
                Company_name=row['Company_name'],
                About_company = row['About_company'],
                Company_link = row['Company_link'],
                Jobrole = row['Jobrole'],
                Job_responsilities = row['Job_responsilities'],
                Job_Salary = row['Job_Salary'],
                Eligibility_cgpa = row['Eligibility_cgpa'],
                Eligibility_branches = row['Eligibility_branches'],
                Eligible_Passedout_Batchs = row['Eligible_Passedout_Batchs'],
                Eligibility_education_gap = row['Eligibility_education_gap'],
                application_start_date =row['application_start_date'],
                application_end_date = row['application_end_date'],
            )
            for row in list_of_dict
        ]
        try:
            msg = Company.objects.bulk_create(objs)
            print('imported successfully')
            return redirect('CompanyList')
        except Exception as e:
            print('Error While Importing Data: ', e)
            returnmsg = {"status_code": 500}
        return JsonResponse(returnmsg)
