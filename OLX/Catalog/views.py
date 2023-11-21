from django.shortcuts import render, get_object_or_404
from Catalog.models import Category
from PushRevelations.models import Revelation
import random

# Create your views here.
def RenderIndex(request):
    if request.method == "POST":
        name = request.POST.get("search")
        revelations = Revelation.objects.filter(name__startswith=name)
        msg = "Результати пошуку"
        if len(revelations) == 0:
            msg = "Нічого не знайдено"
        context = {
            'msg': msg,
            "revelations": revelations,
        }
        return render(request, "search_results.html", context)
    else:
        count_to_fetch = 4
        all_records = Revelation.objects.all()
        random_records = random.sample(list(all_records), count_to_fetch)
        context = {
            'categories': Category.objects.all,
            'revelations': random_records,
        }

        return render(request, 'index.html', context)


def Search__of__category(request, id):
    category = get_object_or_404(Category, id=id)
    revelations = Revelation.objects.filter(category=category)
    msg = "Результати пошуку"
    if len(revelations) == 0:
        msg = "Нічого не знайдено"
    context = {
        "revelations": revelations,
        "msg":msg,
    }

    return render(request, "search_results.html", context)