from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

# ====== import here the models ==============================
from .models import Post
#==============================================================

class BlogListView (ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'



#==============AUTHENTICATION====================================
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "blog/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "blog/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "blog/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "blog/register.html")

# ================ END AUTH SECTION


def contact ( request ):
    contact_form = ContactForm()  
    if contact_form.validate_on_submit():
       username = contact_form.username.data     
       email = contact_form.email.data
       phone = contact_form.phone.data
    return render ('sendemail/contact.html', form = contact_form, mode=4)
    
  
def about( request ):
    return render  ('blog/about.html',title='About', mode=8)
  
def likedPost ( request, postid ):
    return render ('blog/likepost.html', title="Liked Pots", mode=8)