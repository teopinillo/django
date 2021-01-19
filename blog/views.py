from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
from django.views.generic.edit import CreateView, UpdateView


from .models import Post
#==============================================================

class BlogListView (ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # This limits the number of objects per page and adds a paginator
    # and page_obj to the context. See the code inindex.html Django Pagination
    paginate_by = 10

class BlogDetailView ( DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogCreateView ( CreateView ):
    model = Post
    template_name = 'blog/index.html'
    fields = ['title','author','body']

class BlogUpdateView ( UpdateView):
     def get_success_url(self):
        pass #return the appropriate success url   

"""
class EmployerUpdateView(UpdateView):
        model = Employer
        #other stuff.... to be specified

        def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("view-employer", kwargs={"pk": pk})
"""

"""
 In case if want ot use CreateView, you should change urls.py:
 path("new_post", BlogCreateView.as_view(), name="new_post"),

 and in the html

 <form action="" method="post">
 {% csrf_token %}
 {{ form.as_p }}
 < input type="submit" value="Save">
 </form>
"""
@login_required (login_url='/accounts/login/')
@require_http_methods(["POST","GET"])
def index (request):
    if request.method == "POST":
        body = request.POST.get('post_body')
        title = request.POST.get('post_title')
        print (f'title: {title}')
        print (f'body: {body}')
        new_post = Post ( author = request.user, body = body, title = title )
        new_post.save()
        print (f'post [{new_post.pk}] saved')
    
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator (posts, 10)
    page_number = request.GET.get('page')
    limit_posts = paginator.get_page(page_number)
    context = {"posts" : limit_posts}
    return render (request, "blog/index.html", context )


@login_required (login_url='/accounts/login/')
@require_http_methods(["POST"])
def new_post (request):
    if request.method == 'POST':
        body = request.POST.get('post_body')
        title = request.POST.get('post_title')
        print (f'title: {title}')
        print (f'body: {body}')
        new_post = Post ( author = request.user, body = body, title = title )
        new_post.save()
        print (f'post [{new_post.pk}] saved')
        posts = Post.objects.all().order_by('-id')
    paginator = Paginator (posts, 10)
    page_number = request.GET.get('page')
    limit_posts = paginator.get_page(page_number)
    context = {"posts" : limit_posts}
    #return reverse('index', kwargs={'pk': self._id, 'slug': slug})
    return render (request, "blog/index.html", context)

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