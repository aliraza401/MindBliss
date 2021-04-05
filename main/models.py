from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    genderOption = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other') 
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    contact_number = models.CharField(max_length=13)
    gender = models.CharField(
        max_length=10, choices=genderOption, default='Male')
    age = models.SmallIntegerField(null=True)
    email = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

 
class Psychologist(models.Model):
    genderOption = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ) 
    session_feeOption = (
        ('500', '500'),
        ('1000', '1000'),
        ('2000', '2000'),
        ('3000', '3000'),
        ('4000', '4000'),
        ('4000', '4000'),
        ('6000', '6000'),
        ('7000', '7000'),
        ('8000', '8000'),
        ('9000', '9000'),
        ('10000', '10000')
    )
    specializationOption = (
        ('CLINICAL PSYCHOLOGY', 'CLINICAL PSYCHOLOGY'),
        ('COUNSELING PSYCHOLOGY', 'COUNSELING PSYCHOLOGY'),
        ('DEVELOPMENTAL PSYCHOLOGY', 'DEVELOPMENTAL PSYCHOLOGY'),
        ('EDUCATIONAL PSYCHOLOGY', 'EDUCATIONAL PSYCHOLOGY'),
        ('EVIRONMENTAL PSYCHOLOGY', 'EVIRONMENTAL PSYCHOLOGY'),
        ('EXPERIMENTAL PSYCHOLOGY', 'EXPERIMENTAL PSYCHOLOGY'),
        ('FORENSIC PSYCHOLOGY', 'FORENSIC PSYCHOLOGY'),
        ('HUMAN FACTORS PSYCHOLOGY', 'HUMAN FACTORS PSYCHOLOGY'),
        ('SCHOOL PSYCHOLOGY', 'SCHOOL PSYCHOLOGY'),
        ('SOCIAL PSYCHOLOGY', 'SOCIAL PSYCHOLOGY'),
        ('SPORT PSYCHOLOGY', 'SPORT PSYCHOLOGY')
    )
    degreeOption = (
        ('BS PSYCHOLOGY', 'BS PSYCHOLOGY'), 
        ('MS PSYCHOLOGY', 'MS PSYCHOLOGY'),
        ('PHD PSYCHOLOGY', 'PHD PSYCHOLOGY')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    contact_number = models.CharField(max_length=13)
    gender = models.CharField(
        max_length=10, choices=genderOption, default='Male')
    age = models.SmallIntegerField(null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    cnic = models.CharField(max_length=100)
    session_fee = models.CharField(
        max_length=10,  choices=session_feeOption, default='500',)
    specialization = models.CharField(
        max_length=100,  choices=specializationOption,  default='SPORT PSYCHOLOGY')
    degree = models.CharField(
        max_length=100, choices=degreeOption,  default='BS PSYCHOLOGY'
    )
    bio = models.TextField(max_length=200, default=".")


    def __str__(self):
        return self.name
 

class UserStory(models.Model):
    psychologist = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='assignee')
    paitent = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='creator')
    star = models.IntegerField()
    comment = models.TextField(max_length=1500, default='.')

    def __str__(self):
        return self.comment  


class Blog(models.Model):
    psychologist_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self): 
        return self.message
 
 
class Appointment(models.Model):
    psychologist = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, default="" , related_name='assignee1')
    paitent = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, default="", related_name='creator1')
    time = models.TimeField()
    date = models.DateField()
    approved = models.BooleanField(default=False)

    # def __str__(self): 
    #     return self.time
 

class Charge(models.Model):
    appointment = models.ForeignKey(
        Appointment, on_delete=models.SET_NULL, null=True, default="")
    amount = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    # def __str__(self):
    #     return description
   
