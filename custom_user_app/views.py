from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from myuser.models import MyUser

# Create your views here.

def homepage_view(request):
    welcome_name = MyUser.username
    return render(request, "homepage.html", {"welcome_name": welcome_name})

def signup_view(request):
    if request.method == "POST":
        form = Signup_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(username=data.get("username"), passwoed=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = Signup_Form
    return render(request, "generic_form.html", {"form": form})

