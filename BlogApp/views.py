from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def blogs(request):
    categories = Category.objects.all()
    return render(request, 'blog/blogs.html', {'categories': categories})

def contact(request):
    return render(request, 'blog/contact.html')

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
