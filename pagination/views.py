from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import User
from .forms import Userform

def home(request):
    userform = Userform()

    context = {
        "userform": userform
    }
    return render(request, "home.html", context)

def create(request):
    e = []
    if request.method == "POST":
        form = Userform(request.POST)
        errors = form.errors.items()
        name = request.POST["name"]
        email = request.POST["email"]

        if not form.is_valid():
            for key, value in errors:
                e.append(value)
            return HttpResponse(e, content_type = "application/json")
        else:
            User.objects.create(name = name, email = email)
            users = User.objects.all()
            paginator = Paginator(users, 8)
            return redirect("/users/" + str(paginator.num_pages))

def users(request, num):
    users = User.objects.all()
    page = request.GET.get("page", num)

    paginator = Paginator(users, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    return render(request, "users.html", {"users": users} )

#https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html