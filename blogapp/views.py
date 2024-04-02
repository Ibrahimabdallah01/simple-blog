from django.shortcuts import render
from blogapp.models import Post, Comment
from django.http import HttpResponseRedirect
from blogapp.forms import CommentForm

# Create your views here.


def blogapp_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blogapp/index.html", context)


def blogapp_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blogapp/category.html", context)


def blogapp_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blogapp/detail.html", context)
