from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import idcard
from .forms import RegistrationForm
from .forms import LoginForm

# Create your views here.

loggedIn = False

class loginPage(View):
    def get(self, request):
        if loggedIn:
            return render(request, 'checkIn/createnew.html')
        else:
            login_form = LoginForm()
            return render(request, 'checkIn/login.html', {
                'login_form':login_form
            })

class index(View):
    def get(self, request):
        if loggedIn:
            idcardList = idcard.objects.all()
            return render(request, 'checkIn/index.html', {
                'idcardList':idcardList
            })
        else:
             return redirect(reverse('login'))

class createNew(View):
    def get(self, request):
        if loggedIn:
            registration_form = RegistrationForm()
            return render(request, 'checkIn/createnew.html', {
                'registration_form':registration_form
            })
        else:
            return redirect(reverse('login'))

    def post(self, request):
        registration_form = RegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid():
            newid = idcard.objects.create(
            name=registration_form.cleaned_data.get('name'), 
            height_cm=registration_form.cleaned_data.get('height_cm'),
            weight_ib=registration_form.cleaned_data.get('weight_ib'), 
            eye_color=registration_form.cleaned_data.get('eye_color'),
            image = registration_form.cleaned_data.get('image'))
            newid.save()
            return redirect(reverse('index'))
        return render(request, 'checkIn/createnew.html', {
            'form':registration_form
        })




