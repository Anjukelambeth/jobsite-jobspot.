from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator,MinLengthValidator
# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', 
                                message = "Phone number must be entered in the format: '+999999999999'. Up to 13 digits allowed.")
nameMinlength=MinLengthValidator(3,'Min 3 char required')
nameValidator=RegexValidator(regex=r'^[A-Za-z][A-Za-z ]*$',message ="Enter a valid name")

class MyAccountManager(BaseUserManager):
    def create_user(self,user_name,email,phone_number,password=None,*args,**kargs):
        if not email:
            raise ValueError('Username must be there')
        if not user_name:
            raise ValueError('user  must have a username')
        if not phone_number:
            raise ValueError('Provide a valid mobile number')

        user  = self.model(
            email=self.normalize_email(email),
            user_name =  user_name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using= self.db)
        return user
    def create_superuser(self,email,user_name,phone_number,password = None,*args,**kargs):
        user = self.create_user(
            email=self.normalize_email(email),
            user_name=user_name,
            password=password,
            phone_number=phone_number,

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user
class Account(AbstractBaseUser):
    user_name = models.CharField(max_length=50,validators=[nameValidator,nameMinlength])
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=13,validators=[phone_regex],blank=False, unique=True)
    is_js = models.BooleanField(default=False)
    is_rec = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    #required 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    

    #login field
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','phone_number',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm, obj=None):
        return self.is_admin
    def has_module_perms(self, add_label):
        return True
