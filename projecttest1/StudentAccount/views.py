from django.shortcuts import render
import io,csv
from io import TextIOWrapper
from django.views import View
from django.http import HttpResponse,JsonResponse

# Create your views here.
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

