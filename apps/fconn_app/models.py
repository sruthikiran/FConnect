
# Create your models here.

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from localflavor.us.models import USStateField
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

CATEGORIES = (
    ('Early Decision', 'Early Decision'),
    ('Early Action', 'Early Action'),
    ('Single Choice Early Action', 'Single Choice Early Action'),
    ('Regular Decision', 'Regular Decision'),
    ('Rolling Admission', 'Rolling Admission'),
    ('FAFSA', 'FAFSA')
)

STATUS = (
    ('Completed', 'Completed'),
    ('Not Completed', 'Not Completed'),
    ('Not Applicable', 'Not Applicable')
)

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        print(postData['firstName'])
        if len(postData['firstName']) < 1:
            errors["firstname"] = "First Name cannot be empty"
        elif len(postData['firstName']) < 2:
            errors["firstname"] = "First Name should be atleast 2 characters"
        elif not postData['firstName'].isalpha():
            errors["firstname"] = "First Name should contain only letters"

        if len(postData['lastName']) < 1:
            errors["lastname"] = "Last Name cannot be empty"
        elif len(postData['lastName']) < 2:
            errors["lastname"] = "Last Name should be atleast 2 characters"
        elif not postData['lastName'].isalpha():
            errors["lastname"] = "Last Name should contain only letters"

        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty"
        elif not EMAIL_REGEX.match(postData['email']):
                errors["email"] = "Not a Valid Email"
        return errors

    def pwd_validator(self,postData):
        errors = {}
        if len(postData['pwd']) < 1:
            errors["pwd"] = "Password cannot be empty"
        elif len(postData['pwd']) < 8:
            errors["pwd"]= "Password must be more than 8 characters"
        elif len(postData['confpwd']) < 1:
            errors["pwd"] = "Field cannot be empty"
        elif len(postData['confpwd']) < 8:
            errors["confpwd"]= "Password must be more than 8 characters"
        elif not(postData['pwd'] == postData['confpwd']):
            errors["pwd"] = "Passwords don't match! Please enter again"

        return errors

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,blank=True)

    #Additional attributes
    picture = models.ImageField(upload_to = "profile_pics",blank= True,null=True)
    gender = models.CharField(max_length=255,blank= True,null=True)
    birthday = models.DateField(blank= True,null=True)
    address = models.CharField(max_length=255,blank= True,null=True)
    city = models.CharField(max_length=255,blank= True,null=True)
    state = models.CharField(max_length=255,blank= True,null=True)
    schoolState = models.CharField(max_length=255,blank= True,null=True)
    major = models.CharField(max_length=255,blank= True,null=True)
    schoolName = models.CharField(max_length=255,blank= True,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username
    # objects = UserManager()

class College(models.Model):
    user = models.ManyToManyField(User, through="Checklist",related_name="user_colleges")
    # YEAR_Choices = (('2-year/community college','2-year/community college'),('4-year college or university','4-year college or university'))
    # TYPE_Choices = ((Public,'Public'),(Private,'Private'),(For-Profit,'For-Profit'))
    # TYPE_Choices = (('Coed','Coed'),('All Women','All Women'),('All Men','All Men'))
    # SIZE_Choices = (('Small','Small'),('Medium','Medium'),('Large','Large'))
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USStateField(max_length=96,blank=True)
    application_type = models.CharField(max_length=255,choices=CATEGORIES,blank=True)
    deadline = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name + self.city + self.state

class FAFSADeadline(models.Model):
    Federal = 'Federal'
    State = 'State'
    state = USStateField(max_length=96,blank=True)
    FAFSA_Choices = ((Federal,'Federal'),(State,'State'))
    description = models.CharField(max_length=96,choices=FAFSA_Choices)
    notes = models.CharField(max_length = 255, blank=True)
    deadline = models.DateField(null=True,blank=True)
    state_abbr = models.CharField(max_length=24, blank=True)

    #Define the __unicode__ method, which is used by related models by default.
    def __unicode__(self):
        return self.state_abbr

class Checklist(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    application = models.CharField(max_length=96,choices=STATUS)
    test_scores = models.CharField(max_length=96,choices=STATUS)
    school_transcript = models.CharField(max_length=96,choices=STATUS)
    reports = models.CharField(max_length=96,choices=STATUS)
    sec_school_reports = models.CharField(max_length=96,choices=STATUS)
    recommenadtion = models.CharField(max_length=96,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Resource(models.Model):
    title = models.CharField(max_length=255)
    resource_url = models.URLField(blank = True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title + self.resource_url + self.description
