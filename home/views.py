from django.shortcuts import render,redirect
from .models import*
from django.http import HttpResponse
from django.core.serializers import serialize
from .forms import ContactForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .backends import CustomUserBackend


# from reportlab.pdfgen import canvas
from django.conf import settings
import os
# from twilio.rest import Client
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponseNotFound
from io import BytesIO
from django.template.loader import render_to_string

# Create your views here.
def first(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html') 


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')

def dep(request):
    department = Department.objects.all()
    return render(request,'department.html',{'dep':department})  


def doctor(request):
    doctor = Doctors.objects.all()
    return render(request,'doctor.html',{'doc':doctor})


def contact(request):
    department = Department.objects.all()
    doctors = Doctors.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        departments_id = request.POST['departments']
        departments = Department.objects.get(id=departments_id)
        doctor_id = request.POST['doctor']
        doc = Doctors.objects.get(id=doctor_id)
        day = request.POST['day']
        place = request.POST['place']
        contact_data = contactdata.objects.create(name=name,number=number,department=departments,doctors=doc,day=day,place=place)
        try:

            pat = Patients.objects.get(number=number)
            if pat:
                return redirect('final')
        except:
            patients = Patients.objects.create(name=name,doctors=doc,place=place,number=number)   
            return redirect('final')   
    
        


    return render(request, 'contact.html',{'dep':department,'doc':doctors})



# def contact(request):
#     department = Department.objects.all()
#     doctors = Doctors.objects.all()

#     if request.method == 'POST':
#         name = request.POST['name']
#         number = request.POST['number']
#         departments_id = request.POST['departments']
#         departments = Department.objects.get(id=departments_id)
#         doctor_id = request.POST['doctor']
#         doc = Doctors.objects.get(id=doctor_id)
#         day = request.POST['day']
#         place = request.POST['place']
#         contact_data = contactdata.objects.create(name=name, number=number, department=departments, doctors=doc, day=day, place=place)
        
#         # Check if a patient with the given number already exists
#         patient, created = Patients.objects.get_or_create(number=number, defaults={'name': name, 'doctors': doc, 'place': place})

#         if created:
#             return redirect('final')

#     return render(request, 'contact.html', {'dep': department, 'doc': doctors})

      


def final(request):
    return render(request,'final.html')


def doctor_check(request,id):
    print('sdfgh')
    try:
        department = get_object_or_404(Department, pk=id)
        doctors = Doctors.objects.filter(department=department)

        for doctor in doctors:
            print(doctor.name)

        print(doctors)
        # data = {
        #     'doctors':doctors
        # }
        # doctors_data = [{'id':doctor.pk,'name':doctor.name} for doctor in doctors]
        # data = {'doctors_data':doctors_data,}
        serialized_data = serialize('json', doctors)      
        return JsonResponse(serialized_data,safe=False)
    except Doctors.DoesNotExist:
        return JsonResponse({'error': 'Doctors not found'}, status=404)




    
@login_required(login_url='/page/')
def dash(request):
    return render(request, 'admin/dash.html')




@login_required(login_url='/page/')
def hospital_dep(request):
     data = Department.objects.all()
     return render(request, 'admin/department/dep.html',{'data':data})





from django.http import JsonResponse
from .models import Department

def get_total_departments(request):
    total_departments = Department.objects.count()
    data = {'total_departments': total_departments}
    return JsonResponse(data)     



@login_required(login_url='/page/')
def dep_form(request):
    if request.method == "POST":
        name = request.POST['name']
      
        image = request.FILES.get('image')
        data = Department.objects.create(name=name,image=image)
        return redirect('hospital_dep')
        print(data)
    
    return render(request,'admin/department/form.html')




@login_required(login_url='/page/')
def edit(request,id):
    forms = get_object_or_404(Department, id=id)
    if request.method == "POST":
        print(request.POST.get('name'))
        forms.name = request.POST.get('name')
        forms.description = request.POST.get('description')
        forms.image = request.FILES.get('image')
        forms.save()
        print("saved")
        return redirect('hospital_dep')
    return render(request,'admin/department/edit.html',{'forms':forms})




@login_required(login_url='/page/')
def delete(request,id):
    forms = get_object_or_404(Department, id=id)
    forms.delete()
    return redirect('hospital_dep')








@login_required(login_url='/page/')
def hospital_doc(request):
    data = Doctors.objects.all()
    return render(request, 'admin/doctors/doc.html',{'data':data})






@login_required(login_url='/page/')
def doc_form(request):
    dep = Department.objects.all()
    doc = User.objects.filter(doctor=True)
    if request.method == "POST":
        image = request.FILES.get('image')
        monday = request.POST.get('monday') =='on'
        tuesday = request.POST.get('tuesday') =='on'
        wednesday = request.POST.get('wednesday') =='on'
        thursday = request.POST.get('thursday') =='on'
        friday = request.POST.get('friday') == 'on'
        saturday = request.POST.get('saturday') =='on'
        departments_id = request.POST['departments']
        departments = Department.objects.get(id=departments_id)
        user_id = request.POST['doctor']
        users = User.objects.get(id=user_id)
      
    
        data = Doctors.objects.create(name=users,image=image,monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,friday=friday,saturday=saturday,department=departments)
        return redirect('hospital_doc')
        print(data)

     

    
    return render(request,'admin/doctors/form2.html',{'dep':dep,'doc':doc})



from django.http import JsonResponse
from .models import Doctors  # Import your Doctor model

def get_total_doctors(request):
    total_doctors = Doctors.objects.count()  # Count total doctors
    data = {'total_doctors': total_doctors}
    return JsonResponse(data)





@login_required(login_url='/page/')
def edit2(request,id):
    forms = get_object_or_404(Doctors, id=id)
    if request.method == "POST":
        print(request.POST.get('name'))
        forms.name = request.POST.get('name')
        forms.department =request.POST.get('departments')
        
        forms.image = request.FILES.get('image')
        forms.monday = request.POST.get('monday') =='on'
        forms.tuesday = request.POST.get('tuesday') =='on'
        forms.wednesday = request.POST.get('wednesday') =='on'
        forms.thursday = request.POST.get('thursday') =='on'
        forms.friday = request.POST.get('friday')=='on'
        forms.saturday = request.POST.get('saturday') =='on'
        forms.save()
        print("saved")
        return redirect('hospital_doc')
    return render(request,'admin/doctors/edit2.html',{'forms':forms})



@login_required(login_url='/page/')
def delete2(request,id):
    forms = get_object_or_404(Doctors, id=id)
    forms.delete()
    return redirect('hospital_doc')




# def apntmnt(request):
#     return render(request,'admin/appointment/apntmnt.html')

# @login_required(login_url='/page/')
def apntmnt(request):
    appointments = contactdata.objects.all()
    total_appointments = appointments.count() 
    # return render(request, 'admin/appointment/apntmnt.html', {'appointments': appointments, 'total_appointments': total_appointments})
    return render(request, 'admin/appointment/apntmnt.html', {'appointments': appointments})




from django.http import JsonResponse
from .models import contactdata

def get_total_appointments(request):
    total_appointments = contactdata.objects.count()
    data = {'total_appointments': total_appointments}
    return JsonResponse(data)





@login_required(login_url='/page/')
def patient(request):
   
    patient = Patients.objects.all()
    return render(request, 'admin/patients/patient.html', {'patient': patient})




from django.http import JsonResponse
from .models import Patients  # Import your Patients model

def get_total_patients(request):
    total_patients = Patients.objects.count()  # Count total patients
    data = {'total_patients': total_patients}
    return JsonResponse(data)





def LoginPage(request):
    print("dfghjklkj")
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = CustomUserBackend().authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            print('1234567')
            login(request, user)
            return redirect('/dash')
        else:
            error_message ='invalid email or password . please try again'
            return render(request,'page.html',{'error':error_message})
    return render(request,'page.html')






    





# @login_required(login_url='/page/')
def doc_user(request):
        data = User.objects.all()
        return render(request, 'admin/user.html',{'data':data})




@login_required(login_url='/page/')
def add_user(request):
    add = User.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        is_doctor = request.POST.get('is_doctor') 
        if is_doctor == 'on':
            is_doctor= True
        else:
            is_doctor=False

        is_admin = request.POST.get('is_admin')
        if is_admin == 'on':
            is_admin= True
        else:
            is_admin=False 
        data = User.objects.create(name=name,email=email,password=password,doctor=is_doctor,is_admin=is_admin)
        return redirect('user')
    
    
    
    return render(request, 'admin/adduser.html',{'add': add})



@login_required(login_url='/page/')
def edit_user(request,id):
    forms = get_object_or_404(User, id=id)
    if request.method == 'POST':
        forms.name = request.POST.get('name')
        forms.email = request.POST.get('email')
        forms.doctor = request.POST.get('is-doctor') == 'on'
        forms.is_admin = request.POST.get('is-admin') == 'on'
        password = request.POST['password']
        if len(password) > 0:
            forms.password = password
        forms.save()
        return redirect('user')
    return render(request, 'admin/useredit.html',{'forms':forms}) 





# def today(request):
#     today = datetime.now().date()
#       today_date = contactdata.objects.filter(day=today)
#      return render (request,'admin/today.html')


from datetime import datetime

def today(request):
    print(request.user.email)
    email = request.user.email
    doctor_user = User.objects.get(email=email)
    doctors = Doctors.objects.get(name=doctor_user)
    today_date = datetime.now().date()
    appointments_today = contactdata.objects.filter(day=today_date,checked=False,doctors=doctors)
    if today:

      return render(request, 'admin/today.html', {'appointments_today': appointments_today})
    else:
         return render(request, 'admin/today.html', {'message': 'no appointments'})







from datetime import datetime

from datetime import datetime

def upcoming_appointments(request):
    email=request.user.email
    doctor_user = User.objects.get(email=email)
    doctors = Doctors.objects.get(name=doctor_user)
    today_date = datetime.now().date()
    upcoming_appointments = contactdata.objects.filter(day__gt=today_date,checked=False,doctors=doctors)
    if upcoming_appointments:
      return render(request, 'admin/upcoming.html', {'upcoming_appointments': upcoming_appointments})
    else:
         return render(request, 'admin/upcoming.html', {'message': 'no appointments'})



def previous(request):
    today_date = datetime.now().date()
    email = request.user.email
    doctor_user = User.objects.get(email=email)
    doctors = Doctors.objects.get(name=doctor_user)
    previous_appointments = contactdata.objects.filter(day__lt=today_date,doctors=doctors)
    # if previous:
    return render(request, 'admin/previous.html',{'previous_appointments':previous_appointments})
    # else:
    # return render(request, 'admin/previous.html', {'message': 'no appointments'})

    


def pres(request,id):
    contact_data = contactdata.objects.get(id=id)
    if request.method == 'POST':
        p_id=request.POST['id']
        patient = Patients.objects.get(id=p_id)
        pres = request.POST.get('pres')
        image = request.FILES.get('image')
        patient_pres = Prescription.objects.create(prescription=pres,image=image,patients=patient)
        print(patient_pres)
        contact_data.checked= True
        contact_data.save()
        print(contact_data.checked)
     
        return render(request, 'pdf.html', {'data':patient_pres})
        

    number = contact_data.number
    print(number)
    patient = Patients.objects.get(number=number)
    
    if patient:
        return render(request, 'admin/pres.html',{'patient':patient})
    else:
       return render(request, 'admin/today.html')






def pres1(request,id):
    contact_data = contactdata.objects.get(id=id)
    if request.method == 'POST':
        p_id=request.POST['id']
        patient = Patients.objects.get(id=p_id)
        pres = request.POST.get('pres')
        image = request.FILES.get('image')
        patient_pres = Prescription.objects.create(prescription=pres,image=image,patients=patient)
        print(patient_pres)
        contact_data.checked= True
        contact_data.save()
        print(contact_data.checked)
     
        return render(request, 'pdf.html', {'data':patient_pres})
        

    number = contact_data.number
    print(number)
    patient = Patients.objects.get(number=number)
    
    if patient:
        return render(request, 'admin/pres1.html',{'patient':patient})
    else:
       return render(request, 'admin/upcoming.html')






# def table(request,id):
#     patient = Patients.objects.get(id=id)
#     prescrption = Prescription.objects.filter(patients = patient)


#     return render(request, 'admin/table.html',{'pres':prescrption})
    


from django.shortcuts import render, get_object_or_404
from .models import Patients, Prescription

def table(request, id):
    patient = get_object_or_404(Patients, id=id)
    prescription = Prescription.objects.filter(patients=patient)

    return render(request, 'admin/table.html', {'pres': prescription})



def show(request, id):
    contact_data = contactdata.objects.get(id=id)
    number = contact_data.number
    print(number)
    patient = Patients.objects.filter(number=number).first()
    print(patient)
    prescription = Prescription.objects.filter(patients=patient)
    return render(request, 'admin/table.html', {'pres': prescription})







def pdf(request):
    return render(request, 'pdf.html')


@login_required
def logout_function(request):
    logout(request)
    return redirect('/page/')













       


















