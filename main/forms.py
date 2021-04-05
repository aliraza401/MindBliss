from django import forms
from .models import Patient, Psychologist, ContactForm, Blog, UserStory, Appointment, Charge
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'password1', 'password2']


class CreatePaitentForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = [ 'user' ]

        widgets = {
            'contact_number': forms.TextInput(attrs={'placeholder': '+92 xxx xxxxxxxx'}),
        } 

class CreatePsychologistForm(forms.ModelForm):
    class Meta:
        model = Psychologist
        fields = '__all__'
        exclude = [ 'user' ]

        widgets = {
            'contact_number': forms.TextInput(attrs={'placeholder': '+92 xxx xxxxxxxx'}),
        } 


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
 

class CreateBlogForm(forms.ModelForm):
    class Meta: 
        model = Blog
        fields = '__all__' 
        exclude = ['psychologist_id']


class CreateUserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = '__all__'
        exclude = ['paitent', 'psychologist']


class CreateAppointmentForm(forms.ModelForm):
    class Meta: 
        model = Appointment
        fields = '__all__'
        exclude = ['paitent', 'psychologist', 'approved']


class CreateChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = '__all__'
  