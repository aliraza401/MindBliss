from django.contrib import admin
from .models import Psychologist, Paitent, Blog, UserStory, ContactForm

# Register your models here.


admin.site.register(Psychologist)
admin.site.register(Paitent)
admin.site.register(Blog)
admin.site.register(UserStory)
admin.site.register(ContactForm)
