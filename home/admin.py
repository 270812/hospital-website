from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctors)

admin.site.register(Department)
admin.site.register(User)
admin.site.register(contactdata)
admin.site.register(Patients)
admin.site.register(Prescription)