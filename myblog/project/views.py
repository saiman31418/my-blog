from django.contrib.sessions.backends.cache import SessionStore
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import registerForm, PostForm
from .models import register1, post


def register(request):
    form = registerForm()
    msg = 'username already exists'
    context = {
        "form": form,
        "msg": msg
    }
    if request.method == "POST":

        form = registerForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("login")


        else:
            form = registerForm()
            msg = 'username already exists'
            context = {
                "form": form,
                "msg": msg
            }
            return render(request, "register.html", context)


    else:
        form = registerForm()

        context = {
            "form": form,
            "msg": "Hello, Friend!"
        }

    return render(request, "register.html", context)


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        pass1 = request.POST["password"]
        # user=auth.authenticate(username=username,password=pass1)
        ex = register1.objects.get(username=username)

        if username == ex.username and pass1 == ex.password:
            s = SessionStore()
            ex = register1.objects.get(username=ex.username)
            request.session['username'] = ex.username

            context = {
                "ex": ex.username,
                "con": post.objects.filter(username=ex)

            }
            return render(request, "home.html", context)




        else:
            return HttpResponse("invalid")






    else:
        return render(request, "register.html")


def Post(request):
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        username = request.session['username']
        ex = register1.objects.get(username=username)

        p = post(title=title, content=content, username=ex)
        p.save()
        request.session['username'] = ex.username

        context = {
            "ex": ex.username,
            "con": post.objects.filter(username=ex)

        }
        return render(request, "home.html", context)


    else:
        return render(request, "post.html")


def delete(request, id):
    e = post.objects.get(id=id)
    e.delete()
    return redirect("show")


def show(request):
    username = request.session['username']
    ex = register1.objects.get(username=username)

    context = {
        "ex": ex.username,
        "con": post.objects.filter(username=ex)

    }
    return render(request, "home.html", context)


def home(request):
    form = registerForm()
    msg = 'Hello'
    context = {
        "form": form,
        "msg": msg
    }
    return render(request, "register.html", context)
