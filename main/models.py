

from email.policy import default
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import uuid
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length = 255)
    summary = models.CharField(max_length = 400, blank=True)
    logo = models.ImageField(upload_to='company_logos/',default='square-background_23-2148046487.webp',blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    github = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
            
        if not password:
            raise ValueError('Users must have an password')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length = 255 ,verbose_name = 'Your email', unique = True)
    username = models.CharField(max_length=255,unique=True)
    fname = models.CharField(max_length = 255,blank=True)
    lname = models.CharField(max_length = 255, blank=True)
    short_bio = models.CharField(max_length = 255,blank=True)
    long_bio = models.TextField(max_length = 500, blank=True)
    experience = models.CharField(max_length = 100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',default='square-background_23-2148046487.webp',blank=True)
    company = models.ForeignKey(Company, on_delete = models.CASCADE,blank=True, null=True) 
    linkedin = models.URLField(max_length=255, blank=True)
    github = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True    
    
    @property
    def is_staff(self):
        return self.is_active

