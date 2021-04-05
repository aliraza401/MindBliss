from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/',  views.about, name='about'),
    path('signup_patient/',  views.signup_patient, name='signup_patient'),
    path('login/',  views.loginView, name='login'),  
    path('logout/',  views.logoutView, name='logout'),
    path('signup_psychologist/',  views.signup_psychologist,
         name='signup_psychologist'), 
    path('contact_us/',  views.contactUsView,
         name='contact_us'),
    path('search_patient/',  views.searchPatient, name='search_patient'),
    path('create_blog/',  views.ceateBlogView,
         name='create_blog'),
    path('view_blogs/',  views.viewBlogs, 
         name='view_blogs'),
    path('serch_psychologist/',  views.searchPsychologist,
         name='serch_psychologist'),
    path('create_userstory/<int:id>',  views.createUserStory, 
         name='create_userstory'), 
    path('view_psychologist/<int:id>',
         views.viewPsychologist, name='view_psychologist'),
    path('create_appointment/<int:id>',
         views.createAppointment, name='create_appointment'),
    path('charge/<int:id>',
         views.charge, name='charge'),



]
