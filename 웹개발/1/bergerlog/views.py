from django.http import HttpResponse
from django.shortcuts import render
from bergers.models import Berger 


def main(request):
    return render(request, "main.html")

def berger_list(request):
    bergers = Berger.objects.all()

    context = {
        "bergers":bergers,
    }
    return render(request, "berger_list.html", context)

def berger_search(request):
    keyword = request.GET.get("keyword", None)

    if keyword:
        bergers = Berger.objects.filter(name__contains= keyword)

    else:
        bergers = Berger.objects.none()

    context={
        "bergers":bergers,
    }
    return render(request, "berger_search.html", context)

def berger_add(request):
    return render(request, "berger_add.html")