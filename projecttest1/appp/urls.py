from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views

from .views import cuv
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('Studentsignup',views.Studentsignup,name='Studentsignup'),
    
    path('tpo_signup/',views.tpo_signup,name='tpo_signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/',views.loginPage,name='login'),
    path('accounts/logout/',views.logoutUser,name='logout'),

    path('company',views.companySignup,name='companySignup'),
    path('CompanyList',views.CompanyList,name='CompanyList'),
    path('CompaniesVisited',views.CompaniesVisited,name='CompaniesVisited'),
    path('CompanyYetToCome',views.CompanyYetToCome,name='CompanyYetToCome'),
    path('CompanyData/<str:name>/',views.CompanyData,name='CompanyData'),
    path('EligibleCompanies/<int:id>/',views.EligibleCompanies,name='EligibleCompanies'),
    
    path('upload',views.upload,name='upload'),
    path('materials',views.materials_list,name='materials'),
    path('materials/upload',views.upload_materials,name='upload_materials'),
    path('materials/delete/<int:id>',views.delete_materials,name='delete_materials'),
   
    path('StudentFilter',views.StudentFilter,name='StudentFilter'),
    path('StudentsList/<str:name>/',views.StudentsList,name='StudentsList'),
    path('StudentProfileDisplay/<int:stuid>/',views.StudentProfileDisplay,name='StudentProfileDisplay'),
    path('Update_Sprofile/<int:userid>/',views.Update_Sprofile,name='Update_Sprofile'),

    path('password_change/',views.password_change,name='password_change'),
    path('AddPost',views.AddPost,name='AddPost'),
   

   path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

path('mamul',views.mamul,name='mamul'),
path('LoginPage', views.LoginPage,name='LoginPage'),
path('dashboard',views.dashboard,name='dashboard'),
path('profile',views.profile,name='profile'),
path('imex_data',cuv.as_view(),name='imex_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




