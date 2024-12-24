from django.shortcuts import render
from django.http import HttpResponse
import random
from posts.models import Post
# from posts.forms import PostForm


def hello_view ():
    return HttpResponse(f"Hello World {random.randint(1, 100)}")

def html_view(request):
    return render(request, "base.html")

def main_view(request):
    if request.method == 'GET':
     return render(request, 'base.html')

def post_list_view(request):
    if request.method == 'GET':
     posts = Post.objects.all()
     return render(request,"posts/post_list.html", context={"posts":posts})

def post_detail_view(request, id):
    if request.method == 'GET':
     post = Post.objects.get(id=id)
     return render(request,"posts/post_detail.html", context={"post":post})

def post_create_view(request):
    if request.method == 'GET':
        # form = PostForm()
        return render(request,"posts/post_create.html")
    if request.method == 'POST':
        data = request.POST
       # image = request.FILES.get('image')
        title = data.get("title", None)
        description = data.get("description")
       #  print("========" + data("title"))
       #  print("========" + data["description"])
        post = Post.objects.create(title=title, description=description)
        # return HttpResponse (f"POST был создан, id: {post.id}
        return HttpResponse("POST был создан")







