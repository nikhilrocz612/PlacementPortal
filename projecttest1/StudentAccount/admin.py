from django.contrib import admin
from import_export import resources
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class StudentAccountResource(resources.ModelResource):

    class Meta:
        model = StudentAccount
        skip_unchanged = True
        report_skipped = True
        fields = ('id','StudentID','StudentPassword','Student_name','Student_email','Gender','Branch','PhoneNo','Address','Country','Tenth','Twelvth','Present_Cgpa','Total_backlogs','Active_backlogs','Placement_status','TCS','Cognizant','Capgemini','MindTree','Infosys','Wipro','Deloitte','HCL','Accenture','IBM',)
        import_id_fields = ('id',)

class StudentAccountAdmin(ImportExportModelAdmin):
    resource_class = StudentAccountResource 

admin.site.register(StudentAccount, StudentAccountAdmin)