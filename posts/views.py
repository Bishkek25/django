from Tools.scripts.pep384_macrocheck import limited_gen
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.db.models import Q
from posts.models import Post
from posts.forms import PostForm, SearchForm, orderings

from django.contrib.auth.decorators import login_required


"""
posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10, post11, post12, post13, post14, post15]
limit = 3
page = 3

formula:
start = (page - 1) * limit = 8
end = start + limit = 9

"""


def hello_view ():
    return HttpResponse(f"Hello World {random.randint(1, 100)}")

def html_view(request):
    return render(request, "base.html")

def main_view(request):
    if request.method == "GET":
      return render(request, 'base.html')

@login_required(login_url="login-view")
def post_list_view(request):
    if request.method == "GET":
        limit = 4
        page = request.GET.get('page', 1)
        search = request.GET.get("search")
        category = request.GET.get("category")
        form = SearchForm(request.GET)
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            posts = posts.filter(category_id=category)
        if orderings:
            post = posts.order_by(orderings)
        max_page = posts.count() / limit
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]
        context={"posts": posts, "form": form, "max_page": range(1, max_page + 1)}
        return render(
        request,"posts/post_list.html",
        context=context,
    )

@login_required(login_url="login-view")
def post_detail_view(request, id):
    if request.method == "GET":
      limit = 4
      page = request.GET.get("page", 1)
      post = Post.objects.get(id=id)
      return render(request,"posts/post_detail.html", context={"post":post})

@login_required(login_url="login-view")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html",{"form":form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse("форма была неверной")
        # title = data.get("title")
        # description = data.get("description")
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        image = form.cleaned_data['image']
        post = Post.objects.create(title=title, description=description, image=image)
        return HttpResponse(f"Post был создан, id: {post.id}")
    return redirect("/posts/")

           






