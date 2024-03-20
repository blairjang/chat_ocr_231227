from django.shortcuts import render
from blog.models import Post
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    '''
    FBV 방식 게시글 목록 페이지
    '''
    posts = Post.objects.all().order_by("-pk")
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_list.html", context)

# class PostList(ListView):
#     model = Post
#     template_name = "blog/blog_list.html"

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, "blog/single_post_page.html", context)