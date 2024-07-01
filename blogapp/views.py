from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.filter(status='published').order_by('-date_posted')
    return render(request, 'blogapp/home.html', {'posts': posts})
