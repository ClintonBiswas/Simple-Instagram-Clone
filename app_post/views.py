from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from login_app.models import userProfile, Follow
from django.contrib.auth.models import User
from app_post.models import Post
# Create your views here.
@login_required
def homeview(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    if request.method == "GET":
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'app_post/home.html', context={'title': 'Home','search':search, 'result': result, 'posts':posts})
