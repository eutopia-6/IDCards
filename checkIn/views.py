from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import idcard, users, chat
from .forms import RegistrationForm, RegisterAccount, LoginForm, TextForm


# Create your views here.

class loginPage(View):
    def get(self, request):
        #These variables will verify who is logged in and whether they are logged in or not
        global loggedIn
        global userName
        request.session['userName'] = "Blank"
        request.session['loggedIn'] = False
        if request.session['loggedIn']:
            return render(request, 'checkIn/index.html')
        else:
            login_form = LoginForm()
            return render(request, 'checkIn/login.html', {
                'login_form':login_form,
            })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 'username' and 'password' in the .get() are attributes in the LoginForm() class
            # in the forms.py
            # the variable name user and passw doesn't have to match the attribute names
            # below in registerPage view the username and password variable names are actually keyword arguements
            user = login_form.cleaned_data.get('username')
            passw = login_form.cleaned_data.get('password')
            if users.objects.all().filter(username=user).exists() and users.objects.get(username=user).password == passw: 
                request.session['loggedIn'] = True
                request.session['userName'] = user
                return redirect(reverse('success'))
            else:
                return redirect(reverse('register'))
            

class registerPage(View):
    def get(self, request):
        try:
            if request.session['loggedIn']:
                return render(request, 'checkIn/index.html')
            else:
                register_form = RegisterAccount()
                return render(request, 'checkIn/register.html', {
                    'register_form':register_form,
                })
        except:
            return redirect(reverse('login'))
            
    def post(self, request):
        register_form = RegisterAccount(request.POST)
        if register_form.is_valid():
            # the arguments in users.objects.create() are keyword arguments from the models.py for
            # the users class
            # 'username' and 'password' that are in the .get() method are attributes in the
            # RegisterAccount() class in the forms.py
            newUser = users.objects.create(
                username = register_form.cleaned_data.get('username'),
                password = register_form.cleaned_data.get('password'),
            )
            newUser.save() 
            return redirect(reverse('success'))
            


class index(View):
    def get(self, request):
        try:
            if request.session['loggedIn']:
                idcardList = idcard.objects.all()
                return render(request, 'checkIn/index.html', {
                    'idcardList':idcardList
                })
            else:
                return redirect(reverse('login'))
        except:
            return redirect(reverse('login'))

class createNew(View):
    def get(self, request):
        try:
            if request.session['loggedIn']:
                registration_form = RegistrationForm()
                return render(request, 'checkIn/createnew.html', {
                    'registration_form':registration_form
                })
            else:
                return redirect(reverse('login'))
        except:
            return redirect(reverse('login'))

    def post(self, request):
        registration_form = RegistrationForm(request.POST, request.FILES)
        #request.FILES is needed when there are files such as images being posted, otherwise 
        #request.POST is enough
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


class success(View):
    def get(self, request):
        return render(request, 'checkIn/success.html')

class groupChat(View):
    def get(self, request):
        try: 
            if request.session['loggedIn']:
                text_to_post = TextForm()
                chats = chat.objects.all()
                return render(request, 'checkIn/groupchat.html', {
                    'chats':chats,
                    'text_to_post': text_to_post,
                })
            else:
                return redirect(reverse('login'))
        except:
            return redirect(reverse('login'))

    def post(self, request):
        text_to_post = TextForm(request.POST)
        if text_to_post.is_valid():
            text_posted = chat.objects.create(
                text_field = text_to_post.cleaned_data.get('text_to_post'),
                author = request.session['userName']
            )
            return redirect(reverse('groupchat'))

class logoutPage(View):
    def get(self, request):
        return render(request, 'checkin/logout.html')
    def post(self, request):
        request.session['loggedIn'] = False
        request.session['userName'] = 'Blank'
        return redirect(reverse('index'))

