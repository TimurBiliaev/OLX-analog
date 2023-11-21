from django import forms
from SignUp.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['PhoneNumber', 'bio']

class FirstEtapRecovery(forms.Form):
    username = forms.CharField(max_length=65)
    email = forms.EmailField(max_length=65)

