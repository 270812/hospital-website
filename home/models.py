from django.db import models
from django.contrib.auth.models import BaseUserManager,User,AbstractBaseUser,PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError("Users must have email")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
       
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,name,email,password):
        user = self.create_user(
            name=name,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_active =True
        user.is_staff = True
        user.is_superuser = True
        user.doctor = False
        user.save(using=self._db)
        return user
    


class User (AbstractBaseUser):
    name = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(verbose_name='email Address', max_length=40, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    doctor = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True,null=True,blank=True)
    # is_staff = models.BooleanField(default=True,null=True,blank=True)
    # is_admin = models.BooleanField(default=False,null=True,blank=True)
    # is_superuser = models.BooleanField(default=True,null=True,blank=True)
    # doctor = models.BooleanField(default=False,null=True,blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, add_label):
        return True




    




class Department(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    description =models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='departmentimage/',null=True)

    def __str__(self):
        return self.name

class Doctors(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    image = models.ImageField(upload_to="doctorsimage/",null=True,blank=True)
   
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    monday = models.BooleanField(default=False,null=True,blank=True)
    tuesday = models.BooleanField(default=False,null=True,blank=True)
    wednesday= models.BooleanField(default=False,null=True,blank=True)
    thursday = models.BooleanField(default=False,null=True,blank=True)
    friday= models.BooleanField(default=False,null=True,blank=True)
    saturday = models.BooleanField(default=False,null=True,blank=True)
    fees = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name.name

class contactdata(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    number = models.IntegerField(null=True,blank=True)
    department =models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    doctors = models.ForeignKey(Doctors,on_delete=models.CASCADE,null=True,blank=True)
    day = models.DateField(null=True,blank=True)
    place = models.CharField(max_length=20,null=True,blank=True)
    checked = models.BooleanField(default=False,null=True,blank=True)
    Patients= models.CharField(max_length=20,null=True,blank=True)
    

    def __str__(self):
        return self.name

class Patients(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    number= models.IntegerField(null=True,blank=True)
    place = models.CharField(max_length=20,null=True,blank=True)
    doctors = models.ForeignKey(Doctors,on_delete=models.CASCADE,null=True,blank=True)
    


class Prescription(models.Model):
    patients = models.ForeignKey(Patients,on_delete=models.CASCADE,null=True,blank=True)  
    prescription = models.TextField(null=True,blank=True)
    date = models.DateField(null=True,blank=True,auto_now_add=True) 
    image = models.ImageField(upload_to="doctorsimage/",null=True,blank=True)
