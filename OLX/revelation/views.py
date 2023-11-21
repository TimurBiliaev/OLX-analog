from django.shortcuts import render,  get_object_or_404, redirect
from PushRevelations.models import Revelation
import random
from django.contrib.auth.models import User
from revelation.models import RevelationAnswer




def render_revelation(request, id):
    try:
        revelation = get_object_or_404(Revelation, id=id)
        user = revelation.user

        count_to_fetch = 4
        all_records = Revelation.objects.filter(category=revelation.category)
        print(all_records)
        revelations = random.sample(list(all_records), count_to_fetch)

        context = {
            "user": user,
            "revelation": revelation,
            "revelations": revelations,
        }

        return render(request, "revelation.html", context)

    except:
        try:
            revelation = get_object_or_404(Revelation, id=id)
            user = revelation.user

            count_to_fetch = 3
            all_records = Revelation.objects.filter(category=revelation.category)
            print(all_records)
            revelations = random.sample(list(all_records), count_to_fetch)

            context = {
                "user": user,
                "revelation": revelation,
                "revelations": revelations,
            }

            return render(request, "revelation.html", context)
        except:
            try:
                revelation = get_object_or_404(Revelation, id=id)
                user = revelation.user

                count_to_fetch = 2
                all_records = Revelation.objects.filter(category=revelation.category)
                print(all_records)
                revelations = random.sample(list(all_records), count_to_fetch)

                context = {
                    "user": user,
                    "revelation": revelation,
                    "revelations": revelations,
                }

                return render(request, "revelation.html", context)
            except:
                try:
                    revelation = get_object_or_404(Revelation, id=id)
                    user = revelation.user

                    count_to_fetch = 1
                    all_records = Revelation.objects.filter(category=revelation.category)
                    print(all_records)
                    revelations = random.sample(list(all_records), count_to_fetch)

                    context = {
                        "user": user,
                        "revelation": revelation,
                        "revelations": revelations,
                    }

                    return render(request, "revelation.html", context)

                except:
                    revelation = get_object_or_404(Revelation, id=id)
                    user = revelation.user
                    context = {
                        "user": user,
                        "revelation": revelation,
                    }
                    return render(request, "revelation.html", context)




def RenderAnswerForm(request, id):
    if request.method == "POST":
        user_client = request.user
        description = request.POST.get("revelation__answer__description")
        revelation = get_object_or_404(Revelation, id=id)
        user_rev = revelation.user
        data = {
            'revelation': revelation,
            'user_client': user_client,
            'user':user_rev,
            'description':description,
        }


        RevelationAnswer.objects.create(**data)
        return redirect('home')

    else:
        context = {
            "form": 0,
        }

        return render(request, "RevelationAnswer.html", context)



def answer__message(request, id):
    msg_1 = get_object_or_404(RevelationAnswer, id=id)

    if request.method == "POST":
        user_client = request.user
        description = request.POST.get("revelation__answer__description")
        revelation = msg_1.revelation
        user_rev = msg_1.user_client
        print(user_rev.username)
        print(user_client.username)
        data = {
            'revelation': revelation,
            'user_client': user_client,
            'user': user_rev,
            'description': description,
        }

        RevelationAnswer.objects.create(**data)
        return redirect('home')

    else:
        context = {}
        return render(request, "RevelationAnswer.html", context)