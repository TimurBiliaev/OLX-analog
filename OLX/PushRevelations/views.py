from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from PushRevelations.form import PushForm
from PushRevelations.models import Revelation, Gallery
from django.db.models import Max

# Create your views here.

@login_required(login_url='sign_in')
def RenderPushRev(request):
        if request.method == "POST":
                form1 = PushForm(request.POST, request.FILES)
                print(form1.is_valid())
                if form1.is_valid():
                        max_id = Revelation.objects.aggregate(max_id=Max('id'))
                        if max_id['max_id'] is None:
                                max_id = 1
                        else:
                                max_id = max_id['max_id'] + 1
                        revelation_data = form1.cleaned_data
                        revelation_data['user'] = request.user
                        revelation_data['id'] = max_id
                        Revelation.objects.create(**revelation_data)
                        return redirect('home')
                else:
                        form = PushForm()
                        context = {
                                'form': form,
                        }

                        return render(request, 'PushReveletion.html', context)
        else:
                form = PushForm()
                context = {
                        'form': form,
                }

                return render(request, 'PushReveletion.html', context)
