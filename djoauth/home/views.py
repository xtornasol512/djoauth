from django.shortcuts import render

# Create your views here.

def simple_view(request):
    return render(request, "home.html")


def terms(request):
    return render(request, "terms.html")
