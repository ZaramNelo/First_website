from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from .models import Account_owners

# Create your views here.
def Homepage(request):
    return render(request, "homepage.html")

def sign_up(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        number = request.POST.get("number")
        Password = request.POST.get("password")
        hashed_password = make_password(Password)
        if Account_owners.objects.filter(Email=email).exists():
            return render(request,"form_sign_up.html",{
                "message": "This email already exists",
                "name": name,
                "email": email,
                "number":number
            })

        user = Account_owners.objects.create(
            Fullname = name,
            Email = email,
            Number = number,
            password = hashed_password
        )
        request.session["user_id"] = user.id
        return redirect("profile")
    return render(request, "form_sign_up.html")

def Log_in(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not Account_owners.objects.filter(Email=email).exists():
           return render(request, "form_login.html",{
               "message1":"This email does not exist",
               "email": email
           })
        else:
            users = Account_owners.objects.all()
            for user in users:
                if check_password(password,user.password):
                    request.session["user_id"] = user.id
                    return redirect("profile")
            return render(request,"form_login.html",{
                "message2": "This password is incorrect",
                "email": email
                })
        
    return render(request, "form_login.html")

def free_trial(request):
    return render(request, "form_freetrial.html")

def profile(request):
    user_id = request.session["user_id"]
    user = Account_owners.objects.get(id=user_id)
    return render(request, "profile.html",{
        "user":user
    })
