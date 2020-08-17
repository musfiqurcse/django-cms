from django.shortcuts import render
from .models import *
# Create your views here.
def post(request, p_id):
    context = {}
    post = Posts.objects.get(pk=p_id)
    context['post'] = post
    print(post.date)
    return render(request, "post.html",context)


def category(request, c_id):
    context = {}
    print(c_id)
    category = Category.objects.get(pk=c_id)
    context['category'] = category
    posts = Posts.objects.filter(category=category)
    context["posts"] = posts
    return render(request, 'category.html', context)


def blog(request):
    context = {}
    posts = Posts.objects.all()
    context['posts'] = posts
    return render(request, "blog.html", context)