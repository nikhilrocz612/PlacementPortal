from django.contrib import admin
from .models import student,Company,Post,Material
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.



class CompanyResource(resources.ModelResource):

    class Meta:
        model = Company
        skip_unchanged = True
        report_skipped = True
        fields = ('id','Company_name','About_company','Company_link','Jobrole','Job_responsilities','Job_Salary','Eligibility_cgpa','Eligibility_branches','Eligible_Passedout_Batchs','Eligibility_education_gap','application_start_date','application_end_date')
        import_id_fields = ('id',)

class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource

class MaterialResource(resources.ModelResource):

    class Meta:
        model = Material
        skip_unchanged = True
        report_skipped = True
        fields = ('id','FileName','pdf')
        import_id_fields = ('id',)

class MaterialAdmin(ImportExportModelAdmin):
    resource_class = MaterialResource

class PostResource(resources.ModelResource):

    class Meta:
        model = Post
        skip_unchanged = True
        report_skipped = True
        fields =('id','Post_Author','Post_Title','Post_Subject','Post_body')
        import_id_fields = ('id',)

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource

class StudentResource(resources.ModelResource):

    class Meta:
        model = student
        skip_unchanged = True
        report_skipped = True
        fields = ('id','username','student_image','student_name','phone','Address','country','tenth','twelve','cgpa','no_backlog','c_backlog')
        import_id_fields = ('id',)

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource





admin.site.register(Company, CompanyAdmin) 
admin.site.register(Material, MaterialAdmin)
admin.site.register(Post, PostAdmin) 
admin.site.register(student, StudentAdmin)

