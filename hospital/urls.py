"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),

    path('',views.first),
    path('home',views.home, name='home'),
    path('about',views.about,name='about'),
    path('service', views.service, name='service'),
    path('department',views.dep,name='department'),
    path('doctor',views.doctor,name='doctor'),
    path('contact',views.contact,name='contact'),
    path('final',views.final,name='final'),



    # dashboard-------------------------------------------

    path('doctor_check/<int:id>',views.doctor_check),
    path('dash',views.dash,name='dash'),
    path('hospital_dep',views.hospital_dep, name='hospital_dep'),
    path('form',views.dep_form,name='form'),
    path('edit/<int:id>', views.edit, name='editpage'),
    path('delete/<int:id>', views.delete, name='deletepage'),
    path('hosptal_doc',views.hospital_doc, name='hospital_doc'),
    path('form2',views.doc_form,name='form2'),
    path('edit2/<int:id>', views.edit2, name='edit2page'),
    path('delete2/<int:id>', views.delete2, name='delete2page'),
    path('apntmnt',views.apntmnt,name='apntmnt'),
    path('patient',views.patient,name='patient'),
    path('page/',views.LoginPage,name='login_dash'),
    # path('get_department/', views.get_department, name='get_department'),
    path('user',views.doc_user,name='user'),
    # path('user_edit',views.edit_user,name='user_edit'),
    path('add_user',views.add_user,name='add_user'),
    path('user_edit/<int:id>/', views.edit_user, name='user_edit'),
    path('today',views.today, name='today'),
   
    path('upcoming_appointments',views.upcoming_appointments, name='upcoming_appointments'),
    path('previous',views.previous,name='previous'),
    path('pres/<int:id>',views.pres,name='pres'),
    path('pres1/<int:id>',views.pres1,name='pres1'),
    path('table/<int:id>',views.table, name='table'),
    # path('generate-pdf/',views.generate_pdf, name='generate_pdf'),
    # path('download_pdf/<str:filename>/', views.download_pdf, name='download_pdf'),
    path('pdf',views.pdf,name='pdf'),
    path('show/<int:id>',views.show,name='show'),
    # path('html_to_pdf',views.html_to_pdf, name='html_to_pdf')
    path('logout', views.logout_function, name='logout'),
    path('get_total_appointments/',views.get_total_appointments, name='get_total_appointments'),
    path('get_total_departments/',views.get_total_departments, name='get_total_departments'),
    path('get_total_patients/',views.get_total_patients, name='get_total_patients'),
    path('get_total_doctors/',views.get_total_doctors, name='get_total_doctors'),

    
    
]

    
    







urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

