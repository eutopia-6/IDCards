from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Full Name')
    height_cm = forms.IntegerField(label='Height in cm')
    weight_ib = forms.IntegerField(label='Weight in lbs')
    eye_color = forms.CharField(label='Eye Color')
    image = forms.ImageField(label="Your Photo", required=True)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class RegisterAccount(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class TextForm(forms.Form):
    text_to_post = forms.CharField(widget=forms.Textarea)