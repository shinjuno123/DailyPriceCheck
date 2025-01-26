from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

# https://www.amazon.com/Amazon-Fire-TV-Stick-4K-streaming-device/dp/B0CJM1GNFQ/ref=sr_1_1?crid=14IMC0TTGF22E&dib=eyJ2IjoiMSJ9.m3pbep9O4KDkk_evYzvvyoajvL40XxHiiqOqJOuWz_kSrmb0iJjGfACfXWJfZZoBqXOt761QL1M13FWAfyB_bvFLR-mrzDmFq5NtpcCF5XogKK7lCz6lr_X5I9cSRXkmiSHQmnYvkMU2Iv7PWVkkbcOR7LFpWE_LlMVDBSUjBt2g9th4PbXGawU_yK_EjO-Dku38LR5Dl7ieps0T3v9YKtnHdoxvhiZO-wSAL_ANJMY.3he09CNTJ3PlVPHdWvVdEAZ-LtavMzowJqh1nPZZ538&dib_tag=se&keywords=fire+tv+stick&qid=1737611946&sprefix=f%2Caps%2C217&sr=8-1
# Create your models here.
class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name