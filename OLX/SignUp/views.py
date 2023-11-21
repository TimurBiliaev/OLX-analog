from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from SignUp.form import LoginForm, RegisterForm, FirstEtapRecovery, UserDataForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from SignUp.recoverypass import SendMess
from SignUp.models import UserData

# Create your views here.
def RenderSignIn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            username = form.cleaned_data.get("username")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse("Такого користувача немає")

            else:
                mess = "Помилка в веденні даних, спробуйте заново"
                form = LoginForm()
                context = {
                    'mess': mess,
                    'form': form,
                }
                return render(request, 'SignUp.html', context)

    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'SignUp.html', context)


def RenderRegestration(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        userdata_form = UserDataForm(request.POST)
        print(user_form.is_valid())
        if user_form.is_valid() and userdata_form.is_valid():
            user = user_form.save()
            login(request, user)
            PhoneNumber = userdata_form.cleaned_data.get("PhoneNumber")
            bio = userdata_form.cleaned_data.get("bio")
            UserData.objects.create(user=user, PhoneNumber=PhoneNumber, bio=bio)
            return redirect('home')
        else:
            mess = "Помилка в веденні даних, спробуйте заново"
            user_form = RegisterForm()
            userdata_form = UserDataForm()
            context = {
                'mess': mess,
                'user_form': user_form,
                'userdata_form': userdata_form,
            }
            return render(request, 'Regestration.html', context)
    else:
        user_form = RegisterForm()
        userdata_form = UserDataForm()
        context = {
            'user_form': user_form,
            'userdata_form': userdata_form,
        }
        return render(request, 'Regestration.html', context)

def sign_out(request):
    logout(request)
    return redirect('home')

def PasswordRecovery(request):
    if request.method == "POST":
        form = FirstEtapRecovery(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            user = User.objects.filter(email=email, username=username).first()
            if user:
                print(email)
                mess = "HELLO"
                SendMess(email, mess)
                return HttpResponse("Такий користувач є")
            else:
                return HttpResponse("Такого користувача немає")
    else:
        form = FirstEtapRecovery()
        context = {'form': form,}
        return render(request, 'PasswordRecovery.html', context)


