from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm
from django.template.context_processors import request
from user.forms import RegisterForm
from django.contrib.auth.models import User
# from user.models import Profile
from django.contrib.auth import authenticate, login, logout, aget_user
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request,"user/register.html", context={"form":form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request,"user/register.html", context={"form":form})
        elif form.is_valid():
            # form.cleaned_data.__delitem__("password_confirm")
            # image = form.cleaned_data.pop('image')
            # age = form.cleaned_data.pop['age']
            # user = User.objects.create_user(**form.cleaned_data)
            # if user:
            #     Profile.objects.create(user=user, image=image, age=aget_user)
            # elif not user:
            #     form.add_error(None, "User already exists")
            #     return render(request,"user/register.html", context={"form":form})
            # return redirect("main-page")
            # print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            User.objects.create_user(username=username, password=password)
            # return HttpResponse("User created successfully")
            return redirect("main-page")


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,"user/login.html", context={"form": form })
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "user/login.html", context={"form": form})
    #elif form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("main-page")
        if not user:
            form.add_error(None, "invalid username or password")
            return render(request, "user/login.html", context={"form": form})

@login_required(login_url="login-view")
def logout_view(request):
     logout(request)
     return redirect("main-page")

# @login_required(login_url="login-view")
# def profile_view(request):
#     return render(request, "user/profile.html")