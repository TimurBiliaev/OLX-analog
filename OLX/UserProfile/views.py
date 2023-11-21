from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from PushRevelations.models import Revelation
from SignUp.models import UserData
from django.contrib.auth.hashers import check_password
from revelation.models import RevelationAnswer
# Create your views here.

@login_required(login_url='sign_in')
def RenderProfile(request):
    context = {
        'revelations': Revelation.objects.filter(user=request.user)
    }
    return render(request, 'profile.html', context)

@login_required(login_url='sign_in')
def Delete_revelation(request, id):
    revelation = get_object_or_404(Revelation, id=id)
    revelation.delete()
    return redirect('userprofile')

@login_required(login_url='sign_in')
def Edit_revelation(request, id):
    if request.method == "POST":
        reveletion = Revelation.objects.get(id=id)
        reveletion.name = request.POST.get("name")
        reveletion.description = request.POST.get("description")
        reveletion.price = request.POST.get("price")
        reveletion.save()
        return redirect('userprofile')
    else:
        reveletion = Revelation.objects.get(id=id)

        context = {
            'revelation': reveletion,
        }

        return render(request, 'edit.html', context)



def ShowOtherUserProfile(request, id):

    if request.user.id == id:
        return redirect("userprofile")

    user = get_object_or_404(User, id=id)
    revelatinos = Revelation.objects.filter(user=id)
    context = {
        "revelations": revelatinos,
        "user": user,
    }

    return render(request, "otheruserprofile.html", context)


@login_required(login_url='sign_in')
def EditProfile(request):

    context = {
        "user": request.user,
    }

    return render(request,  "editprofile.html", context)


@login_required(login_url='sign_in')
def edit_data(request):

    if request.method == "POST":

        user = request.user
        User_data_object = get_object_or_404(UserData, user_id=user.id)
        User_data_object.bio = request.POST.get("description")
        User_data_object.PhoneNumber = request.POST.get("number")
        User_data_object.save()

        return redirect("dataprofile")

    else:
        user = request.user
        print(user.userdata.bio)
        context = {
            "user": request.user,
        }

        return render(request, "edit_profile.html", context)

def change_password(request):
    if request.method == "POST":
        user = request.user
        old_password = request.POST.get("old_pasw")
        new_pass = request.POST.get("new_pasw")
        new_pass_rep = request.POST.get("new_pasw1")
        if check_password(old_password, user.password):
            if new_pass == new_pass_rep:
                user.set_password(new_pass)
                user.save()
                return redirect("dataprofile")
            else:
                return render(request, "changepassword.html")
        else:
            return render(request, "changepassword.html")
    else:
        return render(request, "changepassword.html")



@login_required(login_url='sign_in')
def delete_profile(request):
    pass


@login_required(login_url='sign_in')
def RenderMessages(request):
    answers = RevelationAnswer.objects.filter(user=request.user)
    your_answers = RevelationAnswer.objects.filter(user_client=request.user)
    msg = ''
    msg_1 = ''
    if len(answers) == 0:
        msg = "Тут не має повідомлень"

    if len(your_answers) == 0:
        msg_1 = "Тут не має повідомлень"

    context = {
        'answers': answers,
        'your_answers': your_answers,
        'msg': msg,
        'msg_1': msg_1,
    }

    return render(request, 'messages.html', context)


@login_required(login_url='sign_in')
def accept_answer(request, id):
    ans = get_object_or_404(RevelationAnswer, id=id)
    answers = RevelationAnswer.objects.filter(revelation=ans.revelation)
    for answer in answers:
        answer.delete()

    return redirect('msg')

@login_required(login_url='sign_in')
def delete_answer(request, id):
    ans = RevelationAnswer.objects.filter(id=id)
    ans.delete()
    return redirect('msg')

