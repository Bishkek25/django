from django.shortcuts import render, HttpResponse, redirect
from user.forms import RegisterForm
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login,logout
# from django.contrib.auth.decorators import Login_required

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request,"user/register.html", context={"form":form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request,"user/register.html", context={"form":form})
        elif form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            User.objects.create(username=username, password=password)
            # return HttpResponse("User created successfully")
            return redirect("main-page")

#
# def login_view(request):
#     if request.metod == "GET":
#       return render(request,"user/login.html", context={"form": form })
#
#
# def logout_view(request):
#      logout(request)
#      return redirect("main-page")
