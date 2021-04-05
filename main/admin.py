

from django.contrib import admin
from .models import Psychologist, Patient, Blog, UserStory, ContactForm, Appointment, Charge

# Register your models here.


admin.site.register(Psychologist)
admin.site.register(Patient)
admin.site.register(Blog)
admin.site.register(UserStory)
admin.site.register(ContactForm)
admin.site.register(Appointment)
admin.site.register(Charge)
 