from django.shortcuts import render, redirect
from PushRevelations.models import Revelation

# Create your views here.
def RenderAdvancedSearch(request):
    if request.method == "POST":
        name = request.POST.get("name")
        start_price = int(request.POST.get("Startprice"))
        finish_price = int(request.POST.get("FinishPrice"))
        revelations = Revelation.objects.filter(name__startswith=name, price__gt=start_price, price__lte=finish_price)
        msg = "Результати пошуку"
        if len(revelations) == 0:
            msg = "Нічого не знайдено"
        context = {
            'revelations': revelations,
            'msg':msg,
        }
        return render(request, "search_results.html", context)
    else:

        return render(request, "advanced_search.html", )


def RenderSearchResults(request, context=None):

    if context is None:
        return redirect("home")

    return render(request, "search_results.html", context)