from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, CreatePaitentForm, CreatePsychologistForm, CreateContactForm, CreateBlogForm, CreateUserStoryForm, CreateAppointmentForm, CreateChargeForm
from django.contrib.auth.decorators import login_required
from .decorators import unacthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .models import Blog, UserStory, Psychologist, Patient, Appointment, Charge
from django.contrib.auth.models import User
from .filters import PsychologistFilter, BLogFilter, PatientFilter
import datetime
import stripe
from django.urls import reverse

stripe.api_key = "sk_test_51IcSMrLmWwONKM69xFGEVp0xQSOLKrPYxZbGitL5R5YqmrYuaxGg8dNAgUuF2WjVmDFSWEAcGZot4zmlJklnfCiW00cVHg4Cpv"


# Create your views here.
# @login_required(login_url='login')


def home(request):
    template = "dashboard.html"
    context = {}

    return render(request, template, context)


def about(request):
    template = "about.html"
    context = {}


@unacthenticated_user
def signup_patient(request):
    template = "signup_patient.html"

    form1 = CreateUserForm()
    form2 = CreatePaitentForm()

    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = CreatePaitentForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            group = Group.objects.get(name="Paitent")
            user.groups.add(group)
            messages.success(request, "patient added success")
            return redirect('login')

    context = {
        'form1': form1,
        'form2': form2,
    }

    return render(request, template, context)


@unacthenticated_user
def signup_psychologist(request):
    template = "signup_psychologist.html"

    form1 = CreateUserForm()
    form2 = CreatePsychologistForm()

    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = CreatePsychologistForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            group = Group.objects.get(name="Psychologist")
            user.groups.add(group)
            messages.success(request, "psychologist added success")
            return redirect('login')

    context = {
        'form1': form1,
        'form2': form2,
    }

    return render(request, template, context)


def loginView(request):
    template = 'login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'invalid username or password')

    context = {}

    return render(request, template, context)


@login_required(login_url='login')
def logoutView(request):
    logout(request)
    messages.info(request, 'logout success')
    return redirect('index')


def contactUsView(request):
    template = "contact_us.html"

    form1 = CreateContactForm()

    if request.method == 'POST':
        form1 = CreateContactForm(request.POST)

        if form1.is_valid():
            form1.save()
            messages.success(
                request, "Thanks for leaving message, we will get back to you in a moment")
            return redirect('index')

    context = {
        'form1': form1,
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=["Psychologist"])
def ceateBlogView(request):
    template = "create_blog.html"

    form1 = CreateBlogForm()

    if request.method == 'POST':
        form1 = CreateBlogForm(request.POST)

        if form1.is_valid():
            blog = form1.save(commit=False)
            blog.psychologist_id = request.user
            blog.save()
            messages.success(
                request, "Blog create success")
            return redirect('index')

    context = {
        'form1': form1,
    }

    return render(request, template, context)


def viewBlogs(request):
    template = "blog_page.html"
    blogs = Blog.objects.all()
    MyFilter = BLogFilter(request.GET, queryset=blogs)
    blogs = MyFilter.qs

    context = {'blogs': blogs, 'filter': MyFilter}
    return render(request, template, context)


def searchPsychologist(request):
    template = "searchpsychologist.html"
    psychologists = Psychologist.objects.all().order_by('-id')

    MyFilter = PsychologistFilter(
        request.GET, queryset=psychologists)
    psychologists = MyFilter.qs
    print(psychologists)

    context = {'psychologists': psychologists, 'MyFilter': MyFilter}

    return render(request, template, context)

 
def searchPatient(request):
    template = "searchpatient.html"
    patients = Patient.objects.all()

    MyFilter = PatientFilter(
        request.GET, queryset=patients)
    patients = MyFilter.qs

    context = {'patients': patients, 'MyFilter': MyFilter}

    return render(request, template, context)


def viewPsychologist(request, id):
    template = "viewpsychologist.html"
    user = User.objects.get(id=id)
    psychologist = Psychologist.objects.get(user=user)
    stories = UserStory.objects.all().filter(psychologist=user)

    context = {'psychologist': psychologist, 'stories': stories}

    return render(request, template, context)


def createUserStory(request, id):
    template = "createUserStory.html"
    user = User.objects.get(id=id)
    psychologist = Psychologist.objects.get(user=user)

    form1 = CreateUserStoryForm()

    if request.method == 'POST':
        form1 = CreateUserStoryForm(request.POST)
        if form1.is_valid():
            blog = form1.save(commit=False)
            blog.paitent = request.user
            blog.psychologist = user
            blog.save()
            messages.success(
                request, "User story created success")
            return redirect('index')

    context = {'form1': form1, "psychologist": psychologist}

    return render(request, template, context)


def createAppointment(request, id):
    template = "createAppointment.html"
    user = User.objects.get(id=id)
    psychologist = Psychologist.objects.get(user=user)
    today = datetime.date.today()
    appointments = Appointment.objects.filter(
        psychologist=user, date__range=[today, today + datetime.timedelta(days=14)])

    form1 = CreateAppointmentForm()

    if request.method == 'POST':
        form1 = CreateAppointmentForm(request.POST)
        print("invalid", form1)
        if form1.is_valid():
            appointment = form1.save(commit=False)
            appointment.paitent = request.user
            appointment.psychologist = user
            print(appointment.date)
            print(appointment.time)

            for app in appointments:
                if app.date == appointment.date and app.time == appointment.time:
                    messages.success(
                        request, "doctor appointment alredy exists, please choose other date")
                    return render(request, template, {'form1': form1, "appointments": appointments})

            appointment.save()
            # messages.success(
            #     request, "appointment reserved, pleasy ")
            app = int(appointment.id)
            return redirect(reverse('charge', kwargs={"id": app}))

    context = {'form1': form1, "appointments": appointments}

    return render(request, template, context)

 
def charge(request, id):
    template = "charge.html"
    patient = Patient.objects.get(user=request.user)
    appointment = Appointment.objects.get(id=id)

    if request.method == 'POST':
        print(request.POST)

        customer = stripe.Customer.create(
            email=patient.email,
            name=patient.name,
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=1000,
            currency="usd",
            description="appointment fee"
        )

        chargeModel = Charge(
            amount = charge.amount/100,
            currency = charge.currency,
            description = charge.description,
            appointment = appointment
        )

        chargeModel.save()
        messages.success(
                request, "Appointment created success")
        return redirect('index')


    context = {}

    return render(request, template, context)
