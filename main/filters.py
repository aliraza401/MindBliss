

import django_filters
from .models import Blog, UserStory, Psychologist, Patient


class PsychologistFilter(django_filters.FilterSet):
    class Meta:
        model = Psychologist 
        fields = ['specialization', 'degree']

 
class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'gender' ]


class BLogFilter(django_filters.FilterSet): 
    class Meta:
        model = Blog
        fields = ['title' ]
 