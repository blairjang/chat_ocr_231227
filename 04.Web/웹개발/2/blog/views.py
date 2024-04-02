from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def post_list(request):
    return render(request, "post_list.html")

def post_detail(request):
    return render(request, "post_detail.html")

def post_add(request):
    return render(request, "post_add.html")